# ModelTestResult

Per-model test results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message about the model test result. | 
**model_id** | **str** | The model ID that was tested. | 
**successful** | **bool** | Whether the model test was successful. | 

## Example

```python
from gooddata_api_client.models.model_test_result import ModelTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTestResult from a JSON string
model_test_result_instance = ModelTestResult.from_json(json)
# print the JSON string representation of the object
print(ModelTestResult.to_json())

# convert the object into a dict
model_test_result_dict = model_test_result_instance.to_dict()
# create an instance of ModelTestResult from a dict
model_test_result_from_dict = ModelTestResult.from_dict(model_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


