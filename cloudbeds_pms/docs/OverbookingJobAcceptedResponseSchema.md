# OverbookingJobAcceptedResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_reference_id** | **int** | Reference ID for tracking via getAsyncApiJob. | 

## Example

```python
from cloudbeds_pms.models.overbooking_job_accepted_response_schema import OverbookingJobAcceptedResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OverbookingJobAcceptedResponseSchema from a JSON string
overbooking_job_accepted_response_schema_instance = OverbookingJobAcceptedResponseSchema.from_json(json)
# print the JSON string representation of the object
print(OverbookingJobAcceptedResponseSchema.to_json())

# convert the object into a dict
overbooking_job_accepted_response_schema_dict = overbooking_job_accepted_response_schema_instance.to_dict()
# create an instance of OverbookingJobAcceptedResponseSchema from a dict
overbooking_job_accepted_response_schema_from_dict = OverbookingJobAcceptedResponseSchema.from_dict(overbooking_job_accepted_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


