# LastRoomValuePutRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Correlation id for tracing this request end-to-end. | 
**data** | [**List[LastRoomValueDecisionSchema]**](LastRoomValueDecisionSchema.md) | Last room value decisions to store. | 
**test_request** | **bool** | Mark as test request (honored in non-production only). | [optional] 

## Example

```python
from cloudbeds_pms.models.last_room_value_put_request_schema import LastRoomValuePutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LastRoomValuePutRequestSchema from a JSON string
last_room_value_put_request_schema_instance = LastRoomValuePutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(LastRoomValuePutRequestSchema.to_json())

# convert the object into a dict
last_room_value_put_request_schema_dict = last_room_value_put_request_schema_instance.to_dict()
# create an instance of LastRoomValuePutRequestSchema from a dict
last_room_value_put_request_schema_from_dict = LastRoomValuePutRequestSchema.from_dict(last_room_value_put_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


