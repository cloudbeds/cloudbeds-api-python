# PostReservationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**reservation_id** | **str** | Reservation identifier | [optional] 
**status** | **str** | Reservation status&lt;br /&gt; &#39;not_confirmed&#39; - Reservation is pending confirmation&lt;br /&gt; &#39;confirmed&#39; - Reservation is confirmed&lt;br /&gt; | [optional] 
**guest_id** | **str** | Guest ID | [optional] 
**guest_first_name** | **str** | Guest First Name | [optional] 
**guest_last_name** | **str** | Guest Last Name | [optional] 
**guest_gender** | **str** | Guest Gender | [optional] 
**guest_email** | **str** | Guest Email | [optional] 
**start_date** | **date** | Reservation CheckIn date | [optional] 
**end_date** | **date** | Reservation CheckOut date | [optional] 
**date_created** | **datetime** | Reservation creation datetime | [optional] 
**grand_total** | **float** | Grand Total | [optional] 
**unassigned** | [**List[PostReservationResponseUnassignedInner]**](PostReservationResponseUnassignedInner.md) | unassigned rooms array | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_reservation_response import PostReservationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationResponse from a JSON string
post_reservation_response_instance = PostReservationResponse.from_json(json)
# print the JSON string representation of the object
print(PostReservationResponse.to_json())

# convert the object into a dict
post_reservation_response_dict = post_reservation_response_instance.to_dict()
# create an instance of PostReservationResponse from a dict
post_reservation_response_from_dict = PostReservationResponse.from_dict(post_reservation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


