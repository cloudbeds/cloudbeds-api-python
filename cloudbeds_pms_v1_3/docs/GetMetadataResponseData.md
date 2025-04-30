# GetMetadataResponseData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**GetMetadataResponseDataApi**](GetMetadataResponseDataApi.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_metadata_response_data import GetMetadataResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataResponseData from a JSON string
get_metadata_response_data_instance = GetMetadataResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMetadataResponseData.to_json())

# convert the object into a dict
get_metadata_response_data_dict = get_metadata_response_data_instance.to_dict()
# create an instance of GetMetadataResponseData from a dict
get_metadata_response_data_from_dict = GetMetadataResponseData.from_dict(get_metadata_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


