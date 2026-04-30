# ClusteringConfig

Clustering configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_clusters** | **int** | Number of clusters to create | 
**threshold** | **float** | Clustering algorithm threshold | 

## Example

```python
from gooddata_api_client.models.clustering_config import ClusteringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteringConfig from a JSON string
clustering_config_instance = ClusteringConfig.from_json(json)
# print the JSON string representation of the object
print(ClusteringConfig.to_json())

# convert the object into a dict
clustering_config_dict = clustering_config_instance.to_dict()
# create an instance of ClusteringConfig from a dict
clustering_config_from_dict = ClusteringConfig.from_dict(clustering_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


