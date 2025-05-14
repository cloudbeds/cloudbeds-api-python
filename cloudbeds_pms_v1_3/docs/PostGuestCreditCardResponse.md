# PostGuestCreditCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_guest_credit_card_response import PostGuestCreditCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGuestCreditCardResponse from a JSON string
post_guest_credit_card_response_instance = PostGuestCreditCardResponse.from_json(json)
# print the JSON string representation of the object
print(PostGuestCreditCardResponse.to_json())

# convert the object into a dict
post_guest_credit_card_response_dict = post_guest_credit_card_response_instance.to_dict()
# create an instance of PostGuestCreditCardResponse from a dict
post_guest_credit_card_response_from_dict = PostGuestCreditCardResponse.from_dict(post_guest_credit_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


