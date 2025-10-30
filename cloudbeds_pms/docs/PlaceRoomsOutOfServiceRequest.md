# PlaceRoomsOutOfServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OutOfServiceRequestSchema]**](OutOfServiceRequestSchema.md) | List of rooms to be placed out of service. | [optional] 

## Example

```python
from cloudbeds_pms.models.place_rooms_out_of_service_request import PlaceRoomsOutOfServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceRoomsOutOfServiceRequest from a JSON string
place_rooms_out_of_service_request_instance = PlaceRoomsOutOfServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PlaceRoomsOutOfServiceRequest.to_json())

# convert the object into a dict
place_rooms_out_of_service_request_dict = place_rooms_out_of_service_request_instance.to_dict()
# create an instance of PlaceRoomsOutOfServiceRequest from a dict
place_rooms_out_of_service_request_from_dict = PlaceRoomsOutOfServiceRequest.from_dict(place_rooms_out_of_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


