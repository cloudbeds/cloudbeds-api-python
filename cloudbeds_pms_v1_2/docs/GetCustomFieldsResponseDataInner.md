# GetCustomFieldsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Unique hotel identifier | [optional] 
**name** | **str** | Field name | [optional] 
**shortcode** | **str** | Internal reference and is used for integration purposes such as custom links and the API | [optional] 
**apply_to** | **str** | Where put this field in reservation or guest section of the booking. | [optional] 
**required** | **bool** | Specify whether this field is required to be filled out. | [optional] 
**is_personal** | **bool** | Specifies if the contents of this field may contain personal information (GDPR). | [optional] 
**max_characters** | **int** | Maximum number of characters allowed to be entered in this field. | [optional] 
**type** | **str** | The field&#39;s input type. | [optional] 
**displayed** | **List[str]** | ¹ Specify where this custom field to show up. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_custom_fields_response_data_inner import GetCustomFieldsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomFieldsResponseDataInner from a JSON string
get_custom_fields_response_data_inner_instance = GetCustomFieldsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetCustomFieldsResponseDataInner.to_json())

# convert the object into a dict
get_custom_fields_response_data_inner_dict = get_custom_fields_response_data_inner_instance.to_dict()
# create an instance of GetCustomFieldsResponseDataInner from a dict
get_custom_fields_response_data_inner_from_dict = GetCustomFieldsResponseDataInner.from_dict(get_custom_fields_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


