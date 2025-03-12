# PostHousekeepingStatusResponseData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for last date/time that the room condition changed | [optional] 
**room_id** | **str** | ID of room | [optional] 
**room_condition** | **str** | New room condition. \&quot;inspected\&quot; status is available only if the property has the feature enabled. | [optional] 
**room_comments** | **str** | New room comments. | [optional] 
**do_not_disturb** | **bool** | New \&quot;do not disturb\&quot; status | [optional] 
**refused_service** | **bool** | New \&quot;refused service\&quot; status | [optional] 
**vacant_pickup** | **bool** | New \&quot;vacant_pickup\&quot; status | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_housekeeping_status_response_data import PostHousekeepingStatusResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostHousekeepingStatusResponseData from a JSON string
post_housekeeping_status_response_data_instance = PostHousekeepingStatusResponseData.from_json(json)
# print the JSON string representation of the object
print(PostHousekeepingStatusResponseData.to_json())

# convert the object into a dict
post_housekeeping_status_response_data_dict = post_housekeeping_status_response_data_instance.to_dict()
# create an instance of PostHousekeepingStatusResponseData from a dict
post_housekeeping_status_response_data_from_dict = PostHousekeepingStatusResponseData.from_dict(post_housekeeping_status_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


