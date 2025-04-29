# PostPutGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**List[PostPatchGroupResponseDataInner]**](PostPatchGroupResponseDataInner.md) | Data | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_put_group_response import PostPutGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostPutGroupResponse from a JSON string
post_put_group_response_instance = PostPutGroupResponse.from_json(json)
# print the JSON string representation of the object
print(PostPutGroupResponse.to_json())

# convert the object into a dict
post_put_group_response_dict = post_put_group_response_instance.to_dict()
# create an instance of PostPutGroupResponse from a dict
post_put_group_response_from_dict = PostPutGroupResponse.from_dict(post_put_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


