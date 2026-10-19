# RedirectResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** | The URL to redirect the user to for authentication | 

## Example

```python
from cloudbeds_pms.models.redirect_response_schema import RedirectResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectResponseSchema from a JSON string
redirect_response_schema_instance = RedirectResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RedirectResponseSchema.to_json())

# convert the object into a dict
redirect_response_schema_dict = redirect_response_schema_instance.to_dict()
# create an instance of RedirectResponseSchema from a dict
redirect_response_schema_from_dict = RedirectResponseSchema.from_dict(redirect_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


