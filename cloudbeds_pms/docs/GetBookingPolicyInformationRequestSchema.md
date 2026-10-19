# GetBookingPolicyInformationRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation identifier. | 
**language_code** | **str** | Language code for the rendered policy text (e.g. \&quot;fr\&quot;, \&quot;en-US\&quot;). Defaults to the property&#39;s language when omitted. | [optional] 

## Example

```python
from cloudbeds_pms.models.get_booking_policy_information_request_schema import GetBookingPolicyInformationRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetBookingPolicyInformationRequestSchema from a JSON string
get_booking_policy_information_request_schema_instance = GetBookingPolicyInformationRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetBookingPolicyInformationRequestSchema.to_json())

# convert the object into a dict
get_booking_policy_information_request_schema_dict = get_booking_policy_information_request_schema_instance.to_dict()
# create an instance of GetBookingPolicyInformationRequestSchema from a dict
get_booking_policy_information_request_schema_from_dict = GetBookingPolicyInformationRequestSchema.from_dict(get_booking_policy_information_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


