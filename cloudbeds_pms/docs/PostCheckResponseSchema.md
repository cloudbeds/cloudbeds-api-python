# PostCheckResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostedCheckResponseSchema**](PostedCheckResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.post_check_response_schema import PostCheckResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostCheckResponseSchema from a JSON string
post_check_response_schema_instance = PostCheckResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostCheckResponseSchema.to_json())

# convert the object into a dict
post_check_response_schema_dict = post_check_response_schema_instance.to_dict()
# create an instance of PostCheckResponseSchema from a dict
post_check_response_schema_from_dict = PostCheckResponseSchema.from_dict(post_check_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


