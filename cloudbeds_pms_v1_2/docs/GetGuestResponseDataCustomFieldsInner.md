# GetGuestResponseDataCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **str** |  | [optional] 
**custom_field_value** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guest_response_data_custom_fields_inner import GetGuestResponseDataCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestResponseDataCustomFieldsInner from a JSON string
get_guest_response_data_custom_fields_inner_instance = GetGuestResponseDataCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(GetGuestResponseDataCustomFieldsInner.to_json())

# convert the object into a dict
get_guest_response_data_custom_fields_inner_dict = get_guest_response_data_custom_fields_inner_instance.to_dict()
# create an instance of GetGuestResponseDataCustomFieldsInner from a dict
get_guest_response_data_custom_fields_inner_from_dict = GetGuestResponseDataCustomFieldsInner.from_dict(get_guest_response_data_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


