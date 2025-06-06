# SortSchema

Represents a list of sort fields to apply to the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[SortFieldSchema]**](SortFieldSchema.md) | The list of fields to sort by | [optional] 

## Example

```python
from cloudbeds_pms.models.sort_schema import SortSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SortSchema from a JSON string
sort_schema_instance = SortSchema.from_json(json)
# print the JSON string representation of the object
print(SortSchema.to_json())

# convert the object into a dict
sort_schema_dict = sort_schema_instance.to_dict()
# create an instance of SortSchema from a dict
sort_schema_from_dict = SortSchema.from_dict(sort_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


