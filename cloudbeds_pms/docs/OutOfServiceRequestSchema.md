# OutOfServiceRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **str** | RFC3339 Date to start the out of service period | 
**to_date** | **str** | RFC3339 Date to end the out of service period | 
**reason** | **str** | Wny is the room out of service? | 

## Example

```python
from cloudbeds_pms.models.out_of_service_request_schema import OutOfServiceRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfServiceRequestSchema from a JSON string
out_of_service_request_schema_instance = OutOfServiceRequestSchema.from_json(json)
# print the JSON string representation of the object
print(OutOfServiceRequestSchema.to_json())

# convert the object into a dict
out_of_service_request_schema_dict = out_of_service_request_schema_instance.to_dict()
# create an instance of OutOfServiceRequestSchema from a dict
out_of_service_request_schema_from_dict = OutOfServiceRequestSchema.from_dict(out_of_service_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


