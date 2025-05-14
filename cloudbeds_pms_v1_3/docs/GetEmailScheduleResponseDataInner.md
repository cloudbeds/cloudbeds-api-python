# GetEmailScheduleResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_schedule_id** | **str** | ID of the email schedule | [optional] 
**name** | **str** | Name of the email schedule | [optional] 
**email_template_id** | **str** | ID of the email template used in this schedule | [optional] 
**template_name** | **str** | Name of the email template used in this schedule | [optional] 
**is_active** | **bool** | True if email template is active; false if not | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_email_schedule_response_data_inner import GetEmailScheduleResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailScheduleResponseDataInner from a JSON string
get_email_schedule_response_data_inner_instance = GetEmailScheduleResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetEmailScheduleResponseDataInner.to_json())

# convert the object into a dict
get_email_schedule_response_data_inner_dict = get_email_schedule_response_data_inner_instance.to_dict()
# create an instance of GetEmailScheduleResponseDataInner from a dict
get_email_schedule_response_data_inner_from_dict = GetEmailScheduleResponseDataInner.from_dict(get_email_schedule_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


