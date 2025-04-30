# GetReservationNotesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_note_id** | **str** | Reservation note ID | [optional] 
**user_name** | **str** | User Name | [optional] 
**date_created** | **datetime** | Creation datetime | [optional] 
**date_modified** | **datetime** | Last modification datetime | [optional] 
**reservation_note** | **str** | Note content | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_notes_response_data_inner import GetReservationNotesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationNotesResponseDataInner from a JSON string
get_reservation_notes_response_data_inner_instance = GetReservationNotesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationNotesResponseDataInner.to_json())

# convert the object into a dict
get_reservation_notes_response_data_inner_dict = get_reservation_notes_response_data_inner_instance.to_dict()
# create an instance of GetReservationNotesResponseDataInner from a dict
get_reservation_notes_response_data_inner_from_dict = GetReservationNotesResponseDataInner.from_dict(get_reservation_notes_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


