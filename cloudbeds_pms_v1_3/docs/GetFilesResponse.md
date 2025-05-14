# GetFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetFilesResponseDataInner]**](GetFilesResponseDataInner.md) | Files linked to the property | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results for supplied parameters | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_files_response import GetFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilesResponse from a JSON string
get_files_response_instance = GetFilesResponse.from_json(json)
# print the JSON string representation of the object
print(GetFilesResponse.to_json())

# convert the object into a dict
get_files_response_dict = get_files_response_instance.to_dict()
# create an instance of GetFilesResponse from a dict
get_files_response_from_dict = GetFilesResponse.from_dict(get_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


