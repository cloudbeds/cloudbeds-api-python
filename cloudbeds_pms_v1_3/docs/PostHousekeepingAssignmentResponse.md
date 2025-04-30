# PostHousekeepingAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_housekeeping_assignment_response import PostHousekeepingAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostHousekeepingAssignmentResponse from a JSON string
post_housekeeping_assignment_response_instance = PostHousekeepingAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(PostHousekeepingAssignmentResponse.to_json())

# convert the object into a dict
post_housekeeping_assignment_response_dict = post_housekeeping_assignment_response_instance.to_dict()
# create an instance of PostHousekeepingAssignmentResponse from a dict
post_housekeeping_assignment_response_from_dict = PostHousekeepingAssignmentResponse.from_dict(post_housekeeping_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


