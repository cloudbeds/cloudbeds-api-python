# GetHousekeepingStatusResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for last date/time that the room condition changed | [optional] 
**room_type_id** | **str** | ID of the room type | [optional] 
**room_type_name** | **str** | Name of the room type | [optional] 
**room_id** | **str** | ID of room | [optional] 
**room_name** | **str** | Name of room | [optional] 
**room_condition** | **str** | Room cleaning condition | [optional] 
**room_occupied** | **bool** | Flag if room currently occupied | [optional] 
**room_blocked** | **bool** | Flag if room is blocked | [optional] 
**frontdesk_status** | **str** | The following frontdesk statuses exist:&lt;br /&gt;&lt;br /&gt; &#39;check-in&#39; - There is no guest checking out, but there is a guest checking in.&lt;br /&gt; &#39;check-out&#39; - Guest checking out today, but no guest checking in.&lt;br /&gt; &#39;stayover&#39; - Guest is in-house, not checking out today and is staying for another night&lt;br /&gt; &#39;turnover&#39; - Guest checking out today and another guest checking in today&lt;br /&gt; &#39;unused&#39; - Room is not being used. There is no one there now due to check out, and no one arriving. | [optional] 
**housekeeper_id** | **str** | ID of Housekeeper | [optional] 
**housekeeper** | **str** | Housekeeper name | [optional] 
**do_not_disturb** | **bool** | Flag if room as set as \&quot;Do Not Disturb\&quot; | [optional] 
**refused_service** | **bool** | Flag if room as set as \&quot;Refused Service\&quot; | [optional] 
**vacant_pickup** | **bool** | Flag if room as set as \&quot;Vacant Pickup\&quot; | [optional] 
**room_comments** | **str** | Room comments | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_housekeeping_status_response_data_inner import GetHousekeepingStatusResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHousekeepingStatusResponseDataInner from a JSON string
get_housekeeping_status_response_data_inner_instance = GetHousekeepingStatusResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetHousekeepingStatusResponseDataInner.to_json())

# convert the object into a dict
get_housekeeping_status_response_data_inner_dict = get_housekeeping_status_response_data_inner_instance.to_dict()
# create an instance of GetHousekeepingStatusResponseDataInner from a dict
get_housekeeping_status_response_data_inner_from_dict = GetHousekeepingStatusResponseDataInner.from_dict(get_housekeeping_status_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


