# PutItemToInventoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_item_to_inventory_response import PutItemToInventoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutItemToInventoryResponse from a JSON string
put_item_to_inventory_response_instance = PutItemToInventoryResponse.from_json(json)
# print the JSON string representation of the object
print(PutItemToInventoryResponse.to_json())

# convert the object into a dict
put_item_to_inventory_response_dict = put_item_to_inventory_response_instance.to_dict()
# create an instance of PutItemToInventoryResponse from a dict
put_item_to_inventory_response_from_dict = PutItemToInventoryResponse.from_dict(put_item_to_inventory_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


