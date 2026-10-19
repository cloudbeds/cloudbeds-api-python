# CardDetailsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last4** | **str** | The last 4 digits of the card number | 
**brand** | **str** | The card brand | 
**payment_method_id** | **UUID** | Identifier of the stored payment method, reusable as paymentMethod.paymentMethodId on a later request. Null when the payment did not store a card. | [optional] 

## Example

```python
from cloudbeds_pms.models.card_details_response_schema import CardDetailsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CardDetailsResponseSchema from a JSON string
card_details_response_schema_instance = CardDetailsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CardDetailsResponseSchema.to_json())

# convert the object into a dict
card_details_response_schema_dict = card_details_response_schema_instance.to_dict()
# create an instance of CardDetailsResponseSchema from a dict
card_details_response_schema_from_dict = CardDetailsResponseSchema.from_dict(card_details_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


