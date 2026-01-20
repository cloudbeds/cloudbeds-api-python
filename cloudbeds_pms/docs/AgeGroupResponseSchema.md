# AgeGroupResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group_type** | **str** |  | 
**min_age** | **int** |  | 
**max_age** | **int** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.age_group_response_schema import AgeGroupResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgeGroupResponseSchema from a JSON string
age_group_response_schema_instance = AgeGroupResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AgeGroupResponseSchema.to_json())

# convert the object into a dict
age_group_response_schema_dict = age_group_response_schema_instance.to_dict()
# create an instance of AgeGroupResponseSchema from a dict
age_group_response_schema_from_dict = AgeGroupResponseSchema.from_dict(age_group_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


