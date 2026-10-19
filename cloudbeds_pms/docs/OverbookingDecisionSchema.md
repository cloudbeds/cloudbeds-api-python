# OverbookingDecisionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Overbooking level: house-wide or per room type. | 
**room_type_id** | **int** | Room Type ID. Required and positive when level is room_type; 0 (or omitted) for house level. | [optional] 
**occupancy_date** | **str** | Occupancy date (YYYY-MM-DD). | 
**overbooking** | **int** | Overbooking limit in the Cloudbeds convention: positive &#x3D; rooms sellable above capacity, negative &#x3D; below. Stored as received (the integration translates its vendor sign). | 
**authorized_capacity** | **int** | Authorized capacity as sent by IDeaS, kept for context/audit. | [optional] 

## Example

```python
from cloudbeds_pms.models.overbooking_decision_schema import OverbookingDecisionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OverbookingDecisionSchema from a JSON string
overbooking_decision_schema_instance = OverbookingDecisionSchema.from_json(json)
# print the JSON string representation of the object
print(OverbookingDecisionSchema.to_json())

# convert the object into a dict
overbooking_decision_schema_dict = overbooking_decision_schema_instance.to_dict()
# create an instance of OverbookingDecisionSchema from a dict
overbooking_decision_schema_from_dict = OverbookingDecisionSchema.from_dict(overbooking_decision_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


