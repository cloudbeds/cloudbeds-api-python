# GetGuestsByFilterResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation&#39;s unique identifier | [optional] 
**guest_name** | **str** |  | [optional] 
**guest_id** | **str** | Guest ID | [optional] 
**room_id** | **str** | Room ID that the guest is assigned | [optional] 
**room_name** | **str** | Name of the room where guest is assigned | [optional] 
**is_main_guest** | **bool** | True if the main guest of the reservation | [optional] 
**is_anonymized** | **bool** | Flag indicating the guest data was removed upon request | [optional] 
**guest_opt_in** | **bool** | If guest has opted-in to marketing communication or not | [optional] 
**is_merged** | **bool** | Flag indicating that guest was merged | [optional] 
**new_guest_id** | **str** | Merged guest ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guests_by_filter_response_data_inner import GetGuestsByFilterResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestsByFilterResponseDataInner from a JSON string
get_guests_by_filter_response_data_inner_instance = GetGuestsByFilterResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGuestsByFilterResponseDataInner.to_json())

# convert the object into a dict
get_guests_by_filter_response_data_inner_dict = get_guests_by_filter_response_data_inner_instance.to_dict()
# create an instance of GetGuestsByFilterResponseDataInner from a dict
get_guests_by_filter_response_data_inner_from_dict = GetGuestsByFilterResponseDataInner.from_dict(get_guests_by_filter_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


