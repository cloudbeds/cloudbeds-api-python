# JobAcceptedResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_reference_id** | **int** | Reference ID for tracking via getAsyncApiJob. | 

## Example

```python
from cloudbeds_pms.models.job_accepted_response_schema import JobAcceptedResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of JobAcceptedResponseSchema from a JSON string
job_accepted_response_schema_instance = JobAcceptedResponseSchema.from_json(json)
# print the JSON string representation of the object
print(JobAcceptedResponseSchema.to_json())

# convert the object into a dict
job_accepted_response_schema_dict = job_accepted_response_schema_instance.to_dict()
# create an instance of JobAcceptedResponseSchema from a dict
job_accepted_response_schema_from_dict = JobAcceptedResponseSchema.from_dict(job_accepted_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


