# PostReservationRequestChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room Type ID | [optional] 
**quantity** | **int** | Number of children for the room type ID | [optional] 
**room_id** | **str** | ID of the individual room | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_reservation_request_children_inner import PostReservationRequestChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationRequestChildrenInner from a JSON string
post_reservation_request_children_inner_instance = PostReservationRequestChildrenInner.from_json(json)
# print the JSON string representation of the object
print(PostReservationRequestChildrenInner.to_json())

# convert the object into a dict
post_reservation_request_children_inner_dict = post_reservation_request_children_inner_instance.to_dict()
# create an instance of PostReservationRequestChildrenInner from a dict
post_reservation_request_children_inner_from_dict = PostReservationRequestChildrenInner.from_dict(post_reservation_request_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


