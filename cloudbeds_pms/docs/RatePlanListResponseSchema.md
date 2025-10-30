# RatePlanListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**data** | [**List[RatePlanResponseSchema]**](RatePlanResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.rate_plan_list_response_schema import RatePlanListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanListResponseSchema from a JSON string
rate_plan_list_response_schema_instance = RatePlanListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanListResponseSchema.to_json())

# convert the object into a dict
rate_plan_list_response_schema_dict = rate_plan_list_response_schema_instance.to_dict()
# create an instance of RatePlanListResponseSchema from a dict
rate_plan_list_response_schema_from_dict = RatePlanListResponseSchema.from_dict(rate_plan_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


