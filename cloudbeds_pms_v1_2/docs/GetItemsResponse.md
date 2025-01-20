# GetItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetItemsResponseDataInner]**](GetItemsResponseDataInner.md) | Item details | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_items_response import GetItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemsResponse from a JSON string
get_items_response_instance = GetItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetItemsResponse.to_json())

# convert the object into a dict
get_items_response_dict = get_items_response_instance.to_dict()
# create an instance of GetItemsResponse from a dict
get_items_response_from_dict = GetItemsResponse.from_dict(get_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


