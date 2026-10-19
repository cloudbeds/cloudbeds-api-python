# StopSellJobAcceptedResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_reference_id** | **int** | Reference ID for tracking via getAsyncApiJob. | 

## Example

```python
from cloudbeds_pms.models.stop_sell_job_accepted_response_schema import StopSellJobAcceptedResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StopSellJobAcceptedResponseSchema from a JSON string
stop_sell_job_accepted_response_schema_instance = StopSellJobAcceptedResponseSchema.from_json(json)
# print the JSON string representation of the object
print(StopSellJobAcceptedResponseSchema.to_json())

# convert the object into a dict
stop_sell_job_accepted_response_schema_dict = stop_sell_job_accepted_response_schema_instance.to_dict()
# create an instance of StopSellJobAcceptedResponseSchema from a dict
stop_sell_job_accepted_response_schema_from_dict = StopSellJobAcceptedResponseSchema.from_dict(stop_sell_job_accepted_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


