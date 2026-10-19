# PosContextSchema

POS source metadata for the request. restaurantName / revenueCenter / mealPeriod / staffReference describe the POS session that produced the request as a whole; they apply uniformly to every item (postCheck) or gratuity entry (postGratuity) in the same POST.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant_name** | **str** | Restaurant or outlet name. | [optional] 
**revenue_center** | **str** | Revenue center identifier. | [optional] 
**meal_period** | **str** | Meal period (e.g., breakfast, lunch, dinner). | [optional] 
**staff_reference** | **str** | Free-text reference to a staff member or terminal in the source POS. | [optional] 

## Example

```python
from cloudbeds_pms.models.pos_context_schema import PosContextSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PosContextSchema from a JSON string
pos_context_schema_instance = PosContextSchema.from_json(json)
# print the JSON string representation of the object
print(PosContextSchema.to_json())

# convert the object into a dict
pos_context_schema_dict = pos_context_schema_instance.to_dict()
# create an instance of PosContextSchema from a dict
pos_context_schema_from_dict = PosContextSchema.from_dict(pos_context_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


