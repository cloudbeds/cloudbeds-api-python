# PostGuestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**guest_id** | **str** | Returns the Guest ID if the request could be completed successfully | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_guest_response import PostGuestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGuestResponse from a JSON string
post_guest_response_instance = PostGuestResponse.from_json(json)
# print the JSON string representation of the object
print(PostGuestResponse.to_json())

# convert the object into a dict
post_guest_response_dict = post_guest_response_instance.to_dict()
# create an instance of PostGuestResponse from a dict
post_guest_response_from_dict = PostGuestResponse.from_dict(post_guest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


