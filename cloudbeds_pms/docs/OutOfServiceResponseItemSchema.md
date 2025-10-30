# OutOfServiceResponseItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The event id of the request | 
**message** | **str** | Response message | [optional] 
**code** | **int** | The HTTP status code of the response | 

## Example

```python
from cloudbeds_pms.models.out_of_service_response_item_schema import OutOfServiceResponseItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfServiceResponseItemSchema from a JSON string
out_of_service_response_item_schema_instance = OutOfServiceResponseItemSchema.from_json(json)
# print the JSON string representation of the object
print(OutOfServiceResponseItemSchema.to_json())

# convert the object into a dict
out_of_service_response_item_schema_dict = out_of_service_response_item_schema_instance.to_dict()
# create an instance of OutOfServiceResponseItemSchema from a dict
out_of_service_response_item_schema_from_dict = OutOfServiceResponseItemSchema.from_dict(out_of_service_response_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


