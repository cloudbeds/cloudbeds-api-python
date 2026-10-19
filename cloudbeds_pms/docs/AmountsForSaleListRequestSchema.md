# AmountsForSaleListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** | Room Type ID. | 
**start_date** | **str** | Start date (YYYY-MM-DD). | 
**end_date** | **str** | End date (YYYY-MM-DD), inclusive. | 

## Example

```python
from cloudbeds_pms.models.amounts_for_sale_list_request_schema import AmountsForSaleListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AmountsForSaleListRequestSchema from a JSON string
amounts_for_sale_list_request_schema_instance = AmountsForSaleListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AmountsForSaleListRequestSchema.to_json())

# convert the object into a dict
amounts_for_sale_list_request_schema_dict = amounts_for_sale_list_request_schema_instance.to_dict()
# create an instance of AmountsForSaleListRequestSchema from a dict
amounts_for_sale_list_request_schema_from_dict = AmountsForSaleListRequestSchema.from_dict(amounts_for_sale_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


