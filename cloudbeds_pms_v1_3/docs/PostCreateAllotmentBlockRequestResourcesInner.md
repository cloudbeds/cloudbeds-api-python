# PostCreateAllotmentBlockRequestResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Existing quote ID (omit to create new) | [optional] 
**resource_type_id** | **str** | Resource type ID | [optional] 
**resource_id** | **str** | Specific resource ID (null for quantity-based) | [optional] 
**resource_type_quantity** | **int** | Quantity (for quantity-based) | [optional] 
**start_at** | **str** | Start date-time (ISO-8601) | [optional] 
**end_at** | **str** | End date-time (ISO-8601) | [optional] 
**interval_rate** | **int** | Rate in cents (e.g. 15000 &#x3D; $150.00) | [optional] 
**interval_type** | **str** | Interval type | [optional] 
**adults** | **int** | Number of adults (default 0) | [optional] 
**children** | **int** | Number of children (default 0) | [optional] 
**inventory_strategy** | **str** | Inventory strategy (RESERVATION or ALLOTMENT) | [optional] 
**title** | **str** | Title of the resource quote | [optional] 
**notes** | **str** | Notes for the resource quote | [optional] 
**event_interval_period** | **str** | Event interval period (minute/hour/day/week/month/year) | [optional] 
**event_interval_amount** | **int** | Event interval amount | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_resources_inner import PostCreateAllotmentBlockRequestResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockRequestResourcesInner from a JSON string
post_create_allotment_block_request_resources_inner_instance = PostCreateAllotmentBlockRequestResourcesInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockRequestResourcesInner.to_json())

# convert the object into a dict
post_create_allotment_block_request_resources_inner_dict = post_create_allotment_block_request_resources_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockRequestResourcesInner from a dict
post_create_allotment_block_request_resources_inner_from_dict = PostCreateAllotmentBlockRequestResourcesInner.from_dict(post_create_allotment_block_request_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


