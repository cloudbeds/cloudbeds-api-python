# GetUnitsResponseSchema

Response for GET /rooms/v1/units

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**List[UnitItemResponseSchema]**](UnitItemResponseSchema.md) | List of units for the property | 

## Example

```python
from cloudbeds_pms.models.get_units_response_schema import GetUnitsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetUnitsResponseSchema from a JSON string
get_units_response_schema_instance = GetUnitsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetUnitsResponseSchema.to_json())

# convert the object into a dict
get_units_response_schema_dict = get_units_response_schema_instance.to_dict()
# create an instance of GetUnitsResponseSchema from a dict
get_units_response_schema_from_dict = GetUnitsResponseSchema.from_dict(get_units_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


