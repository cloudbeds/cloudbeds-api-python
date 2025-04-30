# PostEmailScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**email_schedule_id** | **str** | The ID of the created email schedule. Only present if success &#x3D; true | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_email_schedule_response import PostEmailScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailScheduleResponse from a JSON string
post_email_schedule_response_instance = PostEmailScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(PostEmailScheduleResponse.to_json())

# convert the object into a dict
post_email_schedule_response_dict = post_email_schedule_response_instance.to_dict()
# create an instance of PostEmailScheduleResponse from a dict
post_email_schedule_response_from_dict = PostEmailScheduleResponse.from_dict(post_email_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


