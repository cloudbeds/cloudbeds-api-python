# BadRequestErrorItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.bad_request_error_item_schema import BadRequestErrorItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorItemSchema from a JSON string
bad_request_error_item_schema_instance = BadRequestErrorItemSchema.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorItemSchema.to_json())

# convert the object into a dict
bad_request_error_item_schema_dict = bad_request_error_item_schema_instance.to_dict()
# create an instance of BadRequestErrorItemSchema from a dict
bad_request_error_item_schema_from_dict = BadRequestErrorItemSchema.from_dict(bad_request_error_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


