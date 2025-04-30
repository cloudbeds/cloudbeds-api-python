# PostEmailScheduleRequestScheduleReservationStatusChange



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Specify which reservation status change triggers sending the email | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_email_schedule_request_schedule_reservation_status_change import PostEmailScheduleRequestScheduleReservationStatusChange

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailScheduleRequestScheduleReservationStatusChange from a JSON string
post_email_schedule_request_schedule_reservation_status_change_instance = PostEmailScheduleRequestScheduleReservationStatusChange.from_json(json)
# print the JSON string representation of the object
print(PostEmailScheduleRequestScheduleReservationStatusChange.to_json())

# convert the object into a dict
post_email_schedule_request_schedule_reservation_status_change_dict = post_email_schedule_request_schedule_reservation_status_change_instance.to_dict()
# create an instance of PostEmailScheduleRequestScheduleReservationStatusChange from a dict
post_email_schedule_request_schedule_reservation_status_change_from_dict = PostEmailScheduleRequestScheduleReservationStatusChange.from_dict(post_email_schedule_request_schedule_reservation_status_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


