# PostItemsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation identifier. Required if houseAccountId and groupCode are not provided. | [optional] 
**house_account_id** | **str** | House account identifier. Required if reservationId and groupCode are not provided. | [optional] 
**group_code** | **str** | Group code. Required if reservationId and houseAccountId are not provided. | [optional] 
**sale_date** | **str** | Sale date in RFC 3339 format. If not provided, current timestamp will be used. | [optional] 
**items** | [**List[ItemRequestSchema]**](ItemRequestSchema.md) | Array of items to post (minimum 1 item required) | 

## Example

```python
from cloudbeds_pms.models.post_items_request_schema import PostItemsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostItemsRequestSchema from a JSON string
post_items_request_schema_instance = PostItemsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PostItemsRequestSchema.to_json())

# convert the object into a dict
post_items_request_schema_dict = post_items_request_schema_instance.to_dict()
# create an instance of PostItemsRequestSchema from a dict
post_items_request_schema_from_dict = PostItemsRequestSchema.from_dict(post_items_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


