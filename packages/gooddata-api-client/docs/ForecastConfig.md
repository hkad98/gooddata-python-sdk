# ForecastConfig

Forecast configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_level** | **float** | Confidence interval boundary value. | 
**forecast_period** | **int** | Number of future periods that should be forecasted | 
**seasonal** | **bool** | Whether the input data is seasonal | 

## Example

```python
from gooddata_api_client.models.forecast_config import ForecastConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastConfig from a JSON string
forecast_config_instance = ForecastConfig.from_json(json)
# print the JSON string representation of the object
print(ForecastConfig.to_json())

# convert the object into a dict
forecast_config_dict = forecast_config_instance.to_dict()
# create an instance of ForecastConfig from a dict
forecast_config_from_dict = ForecastConfig.from_dict(forecast_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


