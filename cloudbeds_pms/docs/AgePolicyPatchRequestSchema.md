# AgePolicyPatchRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Age Policy ID. | 
**config** | **str** | Configuration. | 
**extra_guests_config** | **str** | Extra guests configuration. | 
**custom_label** | **str** | Custom label (Adults or Guests) | [optional] 

## Example

```python
from cloudbeds_pms.models.age_policy_patch_request_schema import AgePolicyPatchRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgePolicyPatchRequestSchema from a JSON string
age_policy_patch_request_schema_instance = AgePolicyPatchRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AgePolicyPatchRequestSchema.to_json())

# convert the object into a dict
age_policy_patch_request_schema_dict = age_policy_patch_request_schema_instance.to_dict()
# create an instance of AgePolicyPatchRequestSchema from a dict
age_policy_patch_request_schema_from_dict = AgePolicyPatchRequestSchema.from_dict(age_policy_patch_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


