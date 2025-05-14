# PutGuestRequestGuestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **str** |  | [optional] 
**custom_field_value** | **str** | Custom field value. It&#39;s strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_guest_request_guest_custom_fields_inner import PutGuestRequestGuestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutGuestRequestGuestCustomFieldsInner from a JSON string
put_guest_request_guest_custom_fields_inner_instance = PutGuestRequestGuestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PutGuestRequestGuestCustomFieldsInner.to_json())

# convert the object into a dict
put_guest_request_guest_custom_fields_inner_dict = put_guest_request_guest_custom_fields_inner_instance.to_dict()
# create an instance of PutGuestRequestGuestCustomFieldsInner from a dict
put_guest_request_guest_custom_fields_inner_from_dict = PutGuestRequestGuestCustomFieldsInner.from_dict(put_guest_request_guest_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


