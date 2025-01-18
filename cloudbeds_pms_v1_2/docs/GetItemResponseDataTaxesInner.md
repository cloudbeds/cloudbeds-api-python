# GetItemResponseDataTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_name** | **str** | &lt;sup&gt;2&lt;/sup&gt; Name of the tax | [optional] 
**tax_value** | **float** | &lt;sup&gt;2&lt;/sup&gt; Value of the tax | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_item_response_data_taxes_inner import GetItemResponseDataTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemResponseDataTaxesInner from a JSON string
get_item_response_data_taxes_inner_instance = GetItemResponseDataTaxesInner.from_json(json)
# print the JSON string representation of the object
print(GetItemResponseDataTaxesInner.to_json())

# convert the object into a dict
get_item_response_data_taxes_inner_dict = get_item_response_data_taxes_inner_instance.to_dict()
# create an instance of GetItemResponseDataTaxesInner from a dict
get_item_response_data_taxes_inner_from_dict = GetItemResponseDataTaxesInner.from_dict(get_item_response_data_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


