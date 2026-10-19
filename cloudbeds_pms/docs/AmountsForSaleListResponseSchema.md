# AmountsForSaleListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DateAmountResponseSchema]**](DateAmountResponseSchema.md) | Per-date amounts allotted for sale. | 

## Example

```python
from cloudbeds_pms.models.amounts_for_sale_list_response_schema import AmountsForSaleListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AmountsForSaleListResponseSchema from a JSON string
amounts_for_sale_list_response_schema_instance = AmountsForSaleListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AmountsForSaleListResponseSchema.to_json())

# convert the object into a dict
amounts_for_sale_list_response_schema_dict = amounts_for_sale_list_response_schema_instance.to_dict()
# create an instance of AmountsForSaleListResponseSchema from a dict
amounts_for_sale_list_response_schema_from_dict = AmountsForSaleListResponseSchema.from_dict(amounts_for_sale_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


