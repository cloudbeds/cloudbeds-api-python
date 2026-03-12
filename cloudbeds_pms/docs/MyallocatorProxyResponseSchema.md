# MyallocatorProxyResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the MyAllocator request was successful. | 
**data** | **object** | Response data from MyAllocator. | 
**errors** | **List[object]** | Errors returned by MyAllocator. | 

## Example

```python
from cloudbeds_pms.models.myallocator_proxy_response_schema import MyallocatorProxyResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MyallocatorProxyResponseSchema from a JSON string
myallocator_proxy_response_schema_instance = MyallocatorProxyResponseSchema.from_json(json)
# print the JSON string representation of the object
print(MyallocatorProxyResponseSchema.to_json())

# convert the object into a dict
myallocator_proxy_response_schema_dict = myallocator_proxy_response_schema_instance.to_dict()
# create an instance of MyallocatorProxyResponseSchema from a dict
myallocator_proxy_response_schema_from_dict = MyallocatorProxyResponseSchema.from_dict(myallocator_proxy_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


