# ConflictResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**errors** | [**List[ConflictErrorItemSchema]**](ConflictErrorItemSchema.md) |  | [optional] 
**code** | **str** | Error code identifying the type of conflict | [optional] 

## Example

```python
from cloudbeds_pms.models.conflict_response_schema import ConflictResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictResponseSchema from a JSON string
conflict_response_schema_instance = ConflictResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ConflictResponseSchema.to_json())

# convert the object into a dict
conflict_response_schema_dict = conflict_response_schema_instance.to_dict()
# create an instance of ConflictResponseSchema from a dict
conflict_response_schema_from_dict = ConflictResponseSchema.from_dict(conflict_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


