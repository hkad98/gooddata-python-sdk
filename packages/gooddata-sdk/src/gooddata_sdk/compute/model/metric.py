# (C) 2022 GoodData Corporation
from __future__ import annotations

from typing import Union

import gooddata_api_client.models as afm_models
from pydantic import BaseModel as OpenApiModel

from gooddata_sdk.compute.model.attribute import Attribute
from gooddata_sdk.compute.model.base import ExecModelEntity, Filter, ObjId


def _extract_local_id(val: Union[str, Metric]) -> str:
    if isinstance(val, str):
        return val
    else:
        # if things bomb here it means bad input to model class
        return val.local_id


def _wrap_simple_measure_filter(api_filter):  # type: ignore[no-untyped-def]
    """Wrap a leaf filter into ``FilterDefinitionForSimpleMeasure`` (v7 oneOf)."""
    attribute_cls_names = {"MatchAttributeFilter", "NegativeAttributeFilter", "PositiveAttributeFilter"}
    date_cls_names = {"AbsoluteDateFilter", "AllTimeDateFilter", "RelativeDateFilter"}
    name = type(api_filter).__name__
    if name in attribute_cls_names:
        return afm_models.FilterDefinitionForSimpleMeasure(
            actual_instance=afm_models.AttributeFilter(actual_instance=api_filter)
        )
    if name in date_cls_names:
        return afm_models.FilterDefinitionForSimpleMeasure(
            actual_instance=afm_models.DateFilter(actual_instance=api_filter)
        )
    raise TypeError(f"Unhandled filter type for SimpleMeasureDefinition: {name}")


class Metric(ExecModelEntity):
    def __init__(self, local_id: str) -> None:
        super().__init__()
        self._local_id = local_id

    @property
    def local_id(self) -> str:
        return self._local_id

    def as_api_model(self) -> afm_models.MeasureItem:
        definition = self._body_as_api_model()

        # v7 wraps the variant body in a oneOf envelope (``MeasureItemDefinition``).
        return afm_models.MeasureItem(
            local_identifier=self._local_id,
            definition=afm_models.MeasureItemDefinition(actual_instance=definition),
        )

    def _body_as_api_model(self) -> OpenApiModel:
        raise NotImplementedError()


SIMPLE_METRIC_AGGREGATION = {
    "SUM",
    "AVG",
    "COUNT",
    "APPROXIMATE_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "RUNSUM",
}


class SimpleMetric(Metric):
    def __init__(
        self,
        local_id: str,
        item: ObjId,
        aggregation: str | None = None,
        compute_ratio: bool = False,
        filters: list[Filter] | None = None,
    ) -> None:
        super().__init__(local_id)

        _agg = aggregation.upper() if aggregation is not None else None
        if _agg is not None and _agg not in SIMPLE_METRIC_AGGREGATION:
            raise ValueError(
                f"Invalid simple metric aggregation '{_agg}'. Valid operators: {SIMPLE_METRIC_AGGREGATION}"
            )

        self._item = item

        if item.type == "metric":
            self._aggregation = None
        elif _agg is None:
            self._aggregation = "SUM"
        else:
            self._aggregation = _agg

        self._compute_ratio = compute_ratio

        if filters is None:
            self._filters = []
        else:
            self._filters = filters

    @property
    def item(self) -> ObjId:
        return self._item

    @property
    def aggregation(self) -> str | None:
        return self._aggregation

    @property
    def compute_ratio(self) -> bool:
        return self._compute_ratio

    @property
    def filters(self) -> list[Filter]:
        return self._filters

    def _body_as_api_model(self) -> afm_models.SimpleMeasureDefinition:
        # ``SimpleMeasureDefinitionMeasure.filters`` is typed as
        # ``List[FilterDefinitionForSimpleMeasure]`` — a oneOf envelope
        # wrapping ``AttributeFilter`` or ``DateFilter``, which in turn wrap
        # the leaf filter classes. Build that two-layer envelope here.
        _filters = [_wrap_simple_measure_filter(f.as_api_model()) for f in self.filters]

        # aggregation is optional yet the model bombs if None is sent :(
        if self.aggregation is not None:
            return afm_models.SimpleMeasureDefinition(
                measure=afm_models.SimpleMeasureDefinitionMeasure(
                    item=self.item.as_afm_id_core(),
                    aggregation=self.aggregation,
                    compute_ratio=self.compute_ratio,
                    filters=_filters,
                )
            )
        else:
            return afm_models.SimpleMeasureDefinition(
                measure=afm_models.SimpleMeasureDefinitionMeasure(
                    item=self.item.as_afm_id_core(),
                    compute_ratio=self.compute_ratio,
                    filters=_filters,
                )
            )

    def __repr__(self) -> str:
        return (
            f"compute_model.SimpleMetric("
            f"item='{self.item}', "
            f"aggregation='{self.aggregation}', "
            f"compute_ratio='{self.compute_ratio}', "
            f"filters='{self.filters}')"
        )


class PopDate:
    def __init__(self, attribute: Union[ObjId, Attribute], periods_ago: int) -> None:
        if isinstance(attribute, Attribute):
            self._attribute = attribute.label
        else:
            self._attribute = attribute
        self._periods_ago = periods_ago

    @property
    def attribute(self) -> ObjId:
        return self._attribute

    @property
    def periods_ago(self) -> int:
        return self._periods_ago

    def as_api_model(self) -> afm_models.PopDate:
        return afm_models.PopDate(attribute=self.attribute.as_afm_id_attribute(), periods_ago=self.periods_ago)


class PopDateMetric(Metric):
    def __init__(
        self,
        local_id: str,
        metric: Union[str, Metric],
        date_attributes: list[PopDate],
    ) -> None:
        super().__init__(local_id)

        self._metric = _extract_local_id(metric)
        self._date_attributes = date_attributes

    @property
    def metric_local_id(self) -> str:
        return self._metric

    @property
    def date_attributes(self) -> list[PopDate]:
        return self._date_attributes

    def _body_as_api_model(self) -> afm_models.PopDateMeasureDefinition:
        measure_identifier = afm_models.AfmLocalIdentifier(local_identifier=self.metric_local_id)
        date_attributes = list([a.as_api_model() for a in self.date_attributes])

        return afm_models.PopDateMeasureDefinition(
            over_period_measure=afm_models.PopDateMeasureDefinitionOverPeriodMeasure(
                measure_identifier=measure_identifier, date_attributes=date_attributes
            )
        )


class PopDateDataset:
    def __init__(self, dataset: Union[ObjId, str], periods_ago: int) -> None:
        self._dataset = ObjId(dataset, "dataset") if isinstance(dataset, str) else dataset
        self._periods_ago = periods_ago

    @property
    def dataset(self) -> ObjId:
        return self._dataset

    @property
    def periods_ago(self) -> int:
        return self._periods_ago

    def as_api_model(self) -> afm_models.PopDataset:
        return afm_models.PopDataset(dataset=self.dataset.as_afm_id_dataset(), periods_ago=self.periods_ago)


class PopDatesetMetric(Metric):
    def __init__(
        self,
        local_id: str,
        metric: Union[str, Metric],
        date_datasets: list[PopDateDataset],
    ) -> None:
        super().__init__(local_id)

        self._metric = _extract_local_id(metric)
        self._date_datasets = date_datasets

    @property
    def metric_local_id(self) -> str:
        return self._metric

    @property
    def date_datasets(self) -> list[PopDateDataset]:
        return self._date_datasets

    def _body_as_api_model(self) -> afm_models.PopDatasetMeasureDefinition:
        measure_identifier = afm_models.AfmLocalIdentifier(local_identifier=self.metric_local_id)
        date_datasets = list([d.as_api_model() for d in self.date_datasets])

        return afm_models.PopDatasetMeasureDefinition(
            previous_period_measure=afm_models.PopDatasetMeasureDefinitionPreviousPeriodMeasure(
                measure_identifier=measure_identifier, date_datasets=date_datasets
            )
        )


ARITHMETIC_METRIC_OPERATORS = {
    "SUM",
    "DIFFERENCE",
    "MULTIPLICATION",
    "RATIO",
    "CHANGE",
}


class ArithmeticMetric(Metric):
    def __init__(self, local_id: str, operator: str, operands: list[Union[str, Metric]]) -> None:
        super().__init__(local_id)

        if operator not in ARITHMETIC_METRIC_OPERATORS:
            raise ValueError(
                f"Invalid arithmetic metric operator '{operator}'. Valid operators: {ARITHMETIC_METRIC_OPERATORS}"
            )

        self._operator = operator
        self._operands = list([_extract_local_id(o) for o in operands])

    @property
    def operator(self) -> str:
        return self._operator

    @property
    def operand_local_ids(self) -> list[str]:
        return self._operands

    def _body_as_api_model(self) -> afm_models.ArithmeticMeasureDefinition:
        measure_identifiers = [afm_models.AfmLocalIdentifier(local_identifier=local_d) for local_d in self._operands]

        return afm_models.ArithmeticMeasureDefinition(
            arithmetic_measure=afm_models.ArithmeticMeasureDefinitionArithmeticMeasure(
                operator=self.operator, measure_identifiers=measure_identifiers
            )
        )


class InlineMetric(Metric):
    def __init__(self, maql: str, local_id: str) -> None:
        super().__init__(local_id)
        self._maql = maql

    @property
    def maql(self) -> str:
        return self._maql

    def _body_as_api_model(self) -> afm_models.InlineMeasureDefinition:
        return afm_models.InlineMeasureDefinition(inline=afm_models.InlineMeasureDefinitionInline(maql=self.maql))
