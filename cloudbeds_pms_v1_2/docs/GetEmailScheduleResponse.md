# GetEmailScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetEmailScheduleResponseDataInner]**](GetEmailScheduleResponseDataInner.md) | List of existing email schedules | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_email_schedule_response import GetEmailScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailScheduleResponse from a JSON string
get_email_schedule_response_instance = GetEmailScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailScheduleResponse.to_json())

# convert the object into a dict
get_email_schedule_response_dict = get_email_schedule_response_instance.to_dict()
# create an instance of GetEmailScheduleResponse from a dict
get_email_schedule_response_from_dict = GetEmailScheduleResponse.from_dict(get_email_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


