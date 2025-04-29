# PostEmailScheduleRequestSchedule



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_status_change** | [**PostEmailScheduleRequestScheduleReservationStatusChange**](PostEmailScheduleRequestScheduleReservationStatusChange.md) |  | [optional] 
**reservation_event** | [**PostEmailScheduleRequestScheduleReservationEvent**](PostEmailScheduleRequestScheduleReservationEvent.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_email_schedule_request_schedule import PostEmailScheduleRequestSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailScheduleRequestSchedule from a JSON string
post_email_schedule_request_schedule_instance = PostEmailScheduleRequestSchedule.from_json(json)
# print the JSON string representation of the object
print(PostEmailScheduleRequestSchedule.to_json())

# convert the object into a dict
post_email_schedule_request_schedule_dict = post_email_schedule_request_schedule_instance.to_dict()
# create an instance of PostEmailScheduleRequestSchedule from a dict
post_email_schedule_request_schedule_from_dict = PostEmailScheduleRequestSchedule.from_dict(post_email_schedule_request_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


