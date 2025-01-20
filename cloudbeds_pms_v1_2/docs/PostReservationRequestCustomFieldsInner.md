# PostReservationRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Internal custom field reference. Must match the registered name (shortcode) in backend. Pay Attention | [optional] 
**field_value** | **str** | Custom field value. It&#39;s strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_reservation_request_custom_fields_inner import PostReservationRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationRequestCustomFieldsInner from a JSON string
post_reservation_request_custom_fields_inner_instance = PostReservationRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PostReservationRequestCustomFieldsInner.to_json())

# convert the object into a dict
post_reservation_request_custom_fields_inner_dict = post_reservation_request_custom_fields_inner_instance.to_dict()
# create an instance of PostReservationRequestCustomFieldsInner from a dict
post_reservation_request_custom_fields_inner_from_dict = PostReservationRequestCustomFieldsInner.from_dict(post_reservation_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


