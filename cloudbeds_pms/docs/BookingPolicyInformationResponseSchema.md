# BookingPolicyInformationResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_text** | [**PolicyTextSchema**](PolicyTextSchema.md) |  | 
**scheduled_payments** | [**List[ScheduledPaymentDisplayItemSchema]**](ScheduledPaymentDisplayItemSchema.md) | Upcoming scheduled payments (deposit and installments), pre-formatted for display. Empty for canceled and no-show reservations. | 
**policy_text_source** | **str** | Where policyText came from: \&quot;smart\&quot; when rendered from the reservation&#39;s smart policy, \&quot;legacy\&quot; when it is the property&#39;s legacy cancellation policy text. Null when policyText is null. | 

## Example

```python
from cloudbeds_pms.models.booking_policy_information_response_schema import BookingPolicyInformationResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BookingPolicyInformationResponseSchema from a JSON string
booking_policy_information_response_schema_instance = BookingPolicyInformationResponseSchema.from_json(json)
# print the JSON string representation of the object
print(BookingPolicyInformationResponseSchema.to_json())

# convert the object into a dict
booking_policy_information_response_schema_dict = booking_policy_information_response_schema_instance.to_dict()
# create an instance of BookingPolicyInformationResponseSchema from a dict
booking_policy_information_response_schema_from_dict = BookingPolicyInformationResponseSchema.from_dict(booking_policy_information_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


