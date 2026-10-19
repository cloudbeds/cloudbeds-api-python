# NextActionResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NextActionType**](NextActionType.md) |  | 
**redirect** | [**RedirectResponseSchema**](RedirectResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.next_action_response_schema import NextActionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NextActionResponseSchema from a JSON string
next_action_response_schema_instance = NextActionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(NextActionResponseSchema.to_json())

# convert the object into a dict
next_action_response_schema_dict = next_action_response_schema_instance.to_dict()
# create an instance of NextActionResponseSchema from a dict
next_action_response_schema_from_dict = NextActionResponseSchema.from_dict(next_action_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


