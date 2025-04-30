# GetItemResponseDataFeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | &lt;sup&gt;2&lt;/sup&gt; Name of the fee | [optional] 
**fee_value** | **float** | &lt;sup&gt;2&lt;/sup&gt; Value of the fee | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_item_response_data_fees_inner import GetItemResponseDataFeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemResponseDataFeesInner from a JSON string
get_item_response_data_fees_inner_instance = GetItemResponseDataFeesInner.from_json(json)
# print the JSON string representation of the object
print(GetItemResponseDataFeesInner.to_json())

# convert the object into a dict
get_item_response_data_fees_inner_dict = get_item_response_data_fees_inner_instance.to_dict()
# create an instance of GetItemResponseDataFeesInner from a dict
get_item_response_data_fees_inner_from_dict = GetItemResponseDataFeesInner.from_dict(get_item_response_data_fees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


