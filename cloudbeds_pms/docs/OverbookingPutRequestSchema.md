# OverbookingPutRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Correlation id for tracing this request end-to-end. | 
**data** | [**List[OverbookingDecisionSchema]**](OverbookingDecisionSchema.md) | Overbooking decisions to store. | 
**test_request** | **bool** | Mark as test request (honored in non-production only). | [optional] 

## Example

```python
from cloudbeds_pms.models.overbooking_put_request_schema import OverbookingPutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OverbookingPutRequestSchema from a JSON string
overbooking_put_request_schema_instance = OverbookingPutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(OverbookingPutRequestSchema.to_json())

# convert the object into a dict
overbooking_put_request_schema_dict = overbooking_put_request_schema_instance.to_dict()
# create an instance of OverbookingPutRequestSchema from a dict
overbooking_put_request_schema_from_dict = OverbookingPutRequestSchema.from_dict(overbooking_put_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


