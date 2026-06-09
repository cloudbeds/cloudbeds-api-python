# PostCreateAllotmentBlockResponseDataInnerResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource quote ID | [optional] 
**resource_type_id** | **str** | Resource type ID | [optional] 
**resource_id** | **str** | Resource ID (null for quantity-based) | [optional] 
**resource_type_quantity** | **int** | Quantity of resources | [optional] 
**start_at** | **str** | Start date-time (ISO-8601) | [optional] 
**end_at** | **str** | End date-time (ISO-8601) | [optional] 
**interval_rate** | **int** | Rate in cents (e.g. 15000 &#x3D; $150.00) | [optional] 
**interval_type** | **str** | Interval type | [optional] 
**confirmed** | **bool** | Whether the resource quote is confirmed | [optional] 
**adults** | **int** | Number of adults | [optional] 
**children** | **int** | Number of children | [optional] 
**inventory_strategy** | **str** | Inventory strategy | [optional] 
**allotment_quantity_total** | **int** | Total allotment quantity | [optional] 
**allotment_quantity_consumed** | **int** | Consumed allotment quantity | [optional] 
**resource_type** | **object** | Resource type details | [optional] 
**resource** | **object** | Resource details | [optional] 
**title** | **str** | Title | [optional] 
**notes** | **str** | Notes | [optional] 
**event_interval_period** | **str** | Event interval period | [optional] 
**event_interval_amount** | **int** | Event interval amount | [optional] 
**interval_quantity** | **int** | Interval quantity | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**net_amount** | **object** | Net amount | [optional] 
**subtotal** | **object** | Subtotal | [optional] 
**inclusive_taxes_and_fees_amount** | **object** | Inclusive taxes and fees | [optional] 
**exclusive_taxes_and_fees_amount** | **object** | Exclusive taxes and fees | [optional] 
**total** | **object** | Total | [optional] 
**taxes** | **List[object]** | Applied taxes | [optional] 
**fees** | **List[object]** | Applied fees | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_response_data_inner_resources_inner import PostCreateAllotmentBlockResponseDataInnerResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponseDataInnerResourcesInner from a JSON string
post_create_allotment_block_response_data_inner_resources_inner_instance = PostCreateAllotmentBlockResponseDataInnerResourcesInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponseDataInnerResourcesInner.to_json())

# convert the object into a dict
post_create_allotment_block_response_data_inner_resources_inner_dict = post_create_allotment_block_response_data_inner_resources_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponseDataInnerResourcesInner from a dict
post_create_allotment_block_response_data_inner_resources_inner_from_dict = PostCreateAllotmentBlockResponseDataInnerResourcesInner.from_dict(post_create_allotment_block_response_data_inner_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


