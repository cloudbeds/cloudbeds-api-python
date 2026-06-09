# GetReservationsResponseDataInnerCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_id** | **str** | Unique identifier of the custom field definition (matches /getCustomFields.customFieldID). | [optional] 
**shortcode** | **str** | Stable internal code of the custom field (matches /getCustomFields.shortcode). | [optional] 
**is_active** | **bool** | Whether the custom field definition is active (true) or archived (false). | [optional] 
**custom_field_name** | **str** | Custom Field Name | [optional] 
**custom_field_value** | **str** | Custom Field Value | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_response_data_inner_custom_fields_inner import GetReservationsResponseDataInnerCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsResponseDataInnerCustomFieldsInner from a JSON string
get_reservations_response_data_inner_custom_fields_inner_instance = GetReservationsResponseDataInnerCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsResponseDataInnerCustomFieldsInner.to_json())

# convert the object into a dict
get_reservations_response_data_inner_custom_fields_inner_dict = get_reservations_response_data_inner_custom_fields_inner_instance.to_dict()
# create an instance of GetReservationsResponseDataInnerCustomFieldsInner from a dict
get_reservations_response_data_inner_custom_fields_inner_from_dict = GetReservationsResponseDataInnerCustomFieldsInner.from_dict(get_reservations_response_data_inner_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


