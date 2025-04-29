# PostGuestRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **str** | Custom Field shortcode. | [optional] 
**custom_field_value** | **str** | Custom field value. It&#39;s strictly forbidden to send unencrypted payment data through the API. Numeric values longer than 12 characters and considered valid by Luhn&#39;s algorithm will be rejected. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_guest_request_custom_fields_inner import PostGuestRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostGuestRequestCustomFieldsInner from a JSON string
post_guest_request_custom_fields_inner_instance = PostGuestRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PostGuestRequestCustomFieldsInner.to_json())

# convert the object into a dict
post_guest_request_custom_fields_inner_dict = post_guest_request_custom_fields_inner_instance.to_dict()
# create an instance of PostGuestRequestCustomFieldsInner from a dict
post_guest_request_custom_fields_inner_from_dict = PostGuestRequestCustomFieldsInner.from_dict(post_guest_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


