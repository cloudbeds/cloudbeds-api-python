# GetFilesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | File&#39;s unique identifier | [optional] 
**name** | **str** | File Name | [optional] 
**type** | **str** | File Type | [optional] 
**source** | **str** | File Source | [optional] 
**date_created** | **datetime** | File creation date | [optional] 
**url** | **str** | File&#39;s URL to download | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_files_response_data_inner import GetFilesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilesResponseDataInner from a JSON string
get_files_response_data_inner_instance = GetFilesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetFilesResponseDataInner.to_json())

# convert the object into a dict
get_files_response_data_inner_dict = get_files_response_data_inner_instance.to_dict()
# create an instance of GetFilesResponseDataInner from a dict
get_files_response_data_inner_from_dict = GetFilesResponseDataInner.from_dict(get_files_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


