# GetItemsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item unique identifier | [optional] 
**item_type** | **str** | Item type | [optional] 
**sku** | **str** | Item SKU | [optional] 
**item_code** | **str** | Item code | [optional] 
**name** | **str** | Item name | [optional] 
**category_id** | **str** | Item category identifier. Null if unset | [optional] 
**category_name** | **str** | Item category name. Empty if unset | [optional] 
**description** | **str** | Item description | [optional] 
**price** | **float** | Item price | [optional] 
**stock_inventory** | **bool** | Track stock inventory for this item | [optional] 
**item_quantity** | **int** | &lt;sup&gt;1&lt;/sup&gt; Current amount of item available | [optional] 
**reorder_threshold** | **int** | &lt;sup&gt;1&lt;/sup&gt; Quantity at which to reorder item | [optional] 
**reorder_needed** | **bool** | &lt;sup&gt;1&lt;/sup&gt; true - Whether item is at or below value set for reorder threshold. | [optional] 
**stop_sell** | **int** | &lt;sup&gt;1&lt;/sup&gt; Quantity at which to stop selling product. | [optional] 
**stop_sell_met** | **bool** | &lt;sup&gt;1&lt;/sup&gt; true - Whether item is at or below value set for stop-sell threshold. | [optional] 
**taxes** | [**List[GetItemResponseDataTaxesInner]**](GetItemResponseDataTaxesInner.md) | &lt;sup&gt;2&lt;/sup&gt; Details of the taxes applicable | [optional] 
**total_taxes** | **float** | &lt;sup&gt;2&lt;/sup&gt; Total value of the taxes | [optional] 
**fees** | [**List[GetItemResponseDataFeesInner]**](GetItemResponseDataFeesInner.md) | &lt;sup&gt;2&lt;/sup&gt; Details of the fees applicable | [optional] 
**total_fees** | **float** | &lt;sup&gt;2&lt;/sup&gt; Total value of the fees | [optional] 
**price_without_fees_and_taxes** | **float** | &lt;sup&gt;2&lt;/sup&gt; item price subtracting the included taxes | [optional] 
**grand_total** | **float** | &lt;sup&gt;2&lt;/sup&gt; item price with fees and taxes | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_items_response_data_inner import GetItemsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemsResponseDataInner from a JSON string
get_items_response_data_inner_instance = GetItemsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetItemsResponseDataInner.to_json())

# convert the object into a dict
get_items_response_data_inner_dict = get_items_response_data_inner_instance.to_dict()
# create an instance of GetItemsResponseDataInner from a dict
get_items_response_data_inner_from_dict = GetItemsResponseDataInner.from_dict(get_items_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


