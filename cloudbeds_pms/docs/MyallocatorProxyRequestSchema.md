# MyallocatorProxyRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | MyAllocator endpoint name to proxy the request to. | 
**payload** | **object** | Request payload to forward to MyAllocator. Opaque JSON body. | 

## Example

```python
from cloudbeds_pms.models.myallocator_proxy_request_schema import MyallocatorProxyRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MyallocatorProxyRequestSchema from a JSON string
myallocator_proxy_request_schema_instance = MyallocatorProxyRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MyallocatorProxyRequestSchema.to_json())

# convert the object into a dict
myallocator_proxy_request_schema_dict = myallocator_proxy_request_schema_instance.to_dict()
# create an instance of MyallocatorProxyRequestSchema from a dict
myallocator_proxy_request_schema_from_dict = MyallocatorProxyRequestSchema.from_dict(myallocator_proxy_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


