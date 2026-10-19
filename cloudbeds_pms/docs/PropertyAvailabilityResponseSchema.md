# PropertyAvailabilityResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** |  | 
**property_name** | **str** |  | 
**currency_code** | **str** |  | 
**room_types** | [**List[RoomTypeAvailabilityResponseSchema]**](RoomTypeAvailabilityResponseSchema.md) | Available room types with rates | 

## Example

```python
from cloudbeds_pms.models.property_availability_response_schema import PropertyAvailabilityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAvailabilityResponseSchema from a JSON string
property_availability_response_schema_instance = PropertyAvailabilityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PropertyAvailabilityResponseSchema.to_json())

# convert the object into a dict
property_availability_response_schema_dict = property_availability_response_schema_instance.to_dict()
# create an instance of PropertyAvailabilityResponseSchema from a dict
property_availability_response_schema_from_dict = PropertyAvailabilityResponseSchema.from_dict(property_availability_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


