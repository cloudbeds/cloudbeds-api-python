# GetCustomFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetCustomFieldsResponseDataInner]**](GetCustomFieldsResponseDataInner.md) | Field details | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_custom_fields_response import GetCustomFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomFieldsResponse from a JSON string
get_custom_fields_response_instance = GetCustomFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomFieldsResponse.to_json())

# convert the object into a dict
get_custom_fields_response_dict = get_custom_fields_response_instance.to_dict()
# create an instance of GetCustomFieldsResponse from a dict
get_custom_fields_response_from_dict = GetCustomFieldsResponse.from_dict(get_custom_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


