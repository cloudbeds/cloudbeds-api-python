# ConflictErrorItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**message** | **str** |  | 
**code** | **str** | Error code identifying the specific conflict | [optional] 
**details** | **object** | Additional details about the conflict | [optional] 

## Example

```python
from cloudbeds_pms.models.conflict_error_item_schema import ConflictErrorItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConflictErrorItemSchema from a JSON string
conflict_error_item_schema_instance = ConflictErrorItemSchema.from_json(json)
# print the JSON string representation of the object
print(ConflictErrorItemSchema.to_json())

# convert the object into a dict
conflict_error_item_schema_dict = conflict_error_item_schema_instance.to_dict()
# create an instance of ConflictErrorItemSchema from a dict
conflict_error_item_schema_from_dict = ConflictErrorItemSchema.from_dict(conflict_error_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


