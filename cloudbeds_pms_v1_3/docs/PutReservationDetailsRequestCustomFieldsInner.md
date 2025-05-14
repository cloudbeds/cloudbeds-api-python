# PutReservationDetailsRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **str** | Internal custom field reference. Must match the registered name (shortcode) in backend. Pay Attention | [optional] 
**custom_field_value** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_reservation_details_request_custom_fields_inner import PutReservationDetailsRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutReservationDetailsRequestCustomFieldsInner from a JSON string
put_reservation_details_request_custom_fields_inner_instance = PutReservationDetailsRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PutReservationDetailsRequestCustomFieldsInner.to_json())

# convert the object into a dict
put_reservation_details_request_custom_fields_inner_dict = put_reservation_details_request_custom_fields_inner_instance.to_dict()
# create an instance of PutReservationDetailsRequestCustomFieldsInner from a dict
put_reservation_details_request_custom_fields_inner_from_dict = PutReservationDetailsRequestCustomFieldsInner.from_dict(put_reservation_details_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


