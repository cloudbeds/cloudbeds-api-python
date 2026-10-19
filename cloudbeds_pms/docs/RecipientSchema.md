# RecipientSchema

Recipient attribution for a gratuity. All three fields are optional and independent. When more than one is provided, resolution priority is: userId > email > name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Cloudbeds user ID; must reference a valid user on the property or RECIPIENT_USER_NOT_FOUND is returned. | [optional] 
**email** | **str** | Recipient email; resolved to a user record if userId not provided. | [optional] 
**name** | **str** | Free-text recipient name; always stored as a display string regardless of whether a user record is resolved. | [optional] 

## Example

```python
from cloudbeds_pms.models.recipient_schema import RecipientSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientSchema from a JSON string
recipient_schema_instance = RecipientSchema.from_json(json)
# print the JSON string representation of the object
print(RecipientSchema.to_json())

# convert the object into a dict
recipient_schema_dict = recipient_schema_instance.to_dict()
# create an instance of RecipientSchema from a dict
recipient_schema_from_dict = RecipientSchema.from_dict(recipient_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


