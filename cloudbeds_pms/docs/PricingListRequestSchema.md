# PricingListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_ids** | **List[int]** | List of rate IDs to retrieve pricing for. | 
**start_date** | **date** | Start date filter (YYYY-MM-DD). | [optional] 
**end_date** | **date** | End date filter (YYYY-MM-DD). | [optional] 

## Example

```python
from cloudbeds_pms.models.pricing_list_request_schema import PricingListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingListRequestSchema from a JSON string
pricing_list_request_schema_instance = PricingListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PricingListRequestSchema.to_json())

# convert the object into a dict
pricing_list_request_schema_dict = pricing_list_request_schema_instance.to_dict()
# create an instance of PricingListRequestSchema from a dict
pricing_list_request_schema_from_dict = PricingListRequestSchema.from_dict(pricing_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


