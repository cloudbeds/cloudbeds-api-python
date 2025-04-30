# GetRateJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**has_next_page** | **bool** | Returns true if there is another page of results after this one | [optional] 
**next_page** | **str** | The URL of the next page of results if there is one | [optional] 
**data** | [**List[GetRateJobsResponseDataInner]**](GetRateJobsResponseDataInner.md) | Job details | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_jobs_response import GetRateJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateJobsResponse from a JSON string
get_rate_jobs_response_instance = GetRateJobsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRateJobsResponse.to_json())

# convert the object into a dict
get_rate_jobs_response_dict = get_rate_jobs_response_instance.to_dict()
# create an instance of GetRateJobsResponse from a dict
get_rate_jobs_response_from_dict = GetRateJobsResponse.from_dict(get_rate_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


