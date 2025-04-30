# GetMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **str** | True if property can be found | [optional] 
**data** | [**GetMetadataResponseData**](GetMetadataResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_metadata_response import GetMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataResponse from a JSON string
get_metadata_response_instance = GetMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(GetMetadataResponse.to_json())

# convert the object into a dict
get_metadata_response_dict = get_metadata_response_instance.to_dict()
# create an instance of GetMetadataResponse from a dict
get_metadata_response_from_dict = GetMetadataResponse.from_dict(get_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


