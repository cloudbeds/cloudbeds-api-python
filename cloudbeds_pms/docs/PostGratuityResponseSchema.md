# PostGratuityResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostedGratuityResponseSchema**](PostedGratuityResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.post_gratuity_response_schema import PostGratuityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostGratuityResponseSchema from a JSON string
post_gratuity_response_schema_instance = PostGratuityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostGratuityResponseSchema.to_json())

# convert the object into a dict
post_gratuity_response_schema_dict = post_gratuity_response_schema_instance.to_dict()
# create an instance of PostGratuityResponseSchema from a dict
post_gratuity_response_schema_from_dict = PostGratuityResponseSchema.from_dict(post_gratuity_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


