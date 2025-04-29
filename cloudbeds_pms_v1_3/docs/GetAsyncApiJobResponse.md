# GetAsyncApiJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**has_next_page** | **bool** | Returns true if there is another page of results after this one | [optional] 
**next_page** | **str** | The URL of the next page of results if there is one | [optional] 
**data** | [**List[GetAsyncApiJobResponseDataInner]**](GetAsyncApiJobResponseDataInner.md) | Job details | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_async_api_job_response import GetAsyncApiJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncApiJobResponse from a JSON string
get_async_api_job_response_instance = GetAsyncApiJobResponse.from_json(json)
# print the JSON string representation of the object
print(GetAsyncApiJobResponse.to_json())

# convert the object into a dict
get_async_api_job_response_dict = get_async_api_job_response_instance.to_dict()
# create an instance of GetAsyncApiJobResponse from a dict
get_async_api_job_response_from_dict = GetAsyncApiJobResponse.from_dict(get_async_api_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


