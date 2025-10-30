# AgePolicySingleRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Age Policy ID. | 

## Example

```python
from cloudbeds_pms.models.age_policy_single_request_schema import AgePolicySingleRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicySingleRequestSchema from a JSON string
age_policy_single_request_schema_instance = AgePolicySingleRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AgePolicySingleRequestSchema.to_json())

# convert the object into a dict
age_policy_single_request_schema_dict = age_policy_single_request_schema_instance.to_dict()
# create an instance of AgePolicySingleRequestSchema from a dict
age_policy_single_request_schema_from_dict = AgePolicySingleRequestSchema.from_dict(age_policy_single_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


