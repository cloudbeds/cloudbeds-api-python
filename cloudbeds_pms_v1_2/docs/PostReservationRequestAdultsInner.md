# PostReservationRequestAdultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room Type ID | [optional] 
**quantity** | **int** | Quantity of adults for the room type ID | [optional] 
**room_id** | **str** | ID of the individual room | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_reservation_request_adults_inner import PostReservationRequestAdultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationRequestAdultsInner from a JSON string
post_reservation_request_adults_inner_instance = PostReservationRequestAdultsInner.from_json(json)
# print the JSON string representation of the object
print(PostReservationRequestAdultsInner.to_json())

# convert the object into a dict
post_reservation_request_adults_inner_dict = post_reservation_request_adults_inner_instance.to_dict()
# create an instance of PostReservationRequestAdultsInner from a dict
post_reservation_request_adults_inner_from_dict = PostReservationRequestAdultsInner.from_dict(post_reservation_request_adults_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


