# PostEmailScheduleRequestScheduleReservationEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Specify event that triggers email sending | [optional] 
**days** | **int** | Number of days prior to or after the event | [optional] 
**time** | **str** | Time of the day | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_email_schedule_request_schedule_reservation_event import PostEmailScheduleRequestScheduleReservationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailScheduleRequestScheduleReservationEvent from a JSON string
post_email_schedule_request_schedule_reservation_event_instance = PostEmailScheduleRequestScheduleReservationEvent.from_json(json)
# print the JSON string representation of the object
print(PostEmailScheduleRequestScheduleReservationEvent.to_json())

# convert the object into a dict
post_email_schedule_request_schedule_reservation_event_dict = post_email_schedule_request_schedule_reservation_event_instance.to_dict()
# create an instance of PostEmailScheduleRequestScheduleReservationEvent from a dict
post_email_schedule_request_schedule_reservation_event_from_dict = PostEmailScheduleRequestScheduleReservationEvent.from_dict(post_email_schedule_request_schedule_reservation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


