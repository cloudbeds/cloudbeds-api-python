# EligibleRatesRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**sort** | [**SortSchema**](SortSchema.md) |  | [optional] 
**start_date** | **date** | Start date of the date range to filter rate plans. | 
**end_date** | **date** | End date of the date range to filter rate plans. | 

## Example

```python
from cloudbeds_pms.models.eligible_rates_request_schema import EligibleRatesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleRatesRequestSchema from a JSON string
eligible_rates_request_schema_instance = EligibleRatesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EligibleRatesRequestSchema.to_json())

# convert the object into a dict
eligible_rates_request_schema_dict = eligible_rates_request_schema_instance.to_dict()
# create an instance of EligibleRatesRequestSchema from a dict
eligible_rates_request_schema_from_dict = EligibleRatesRequestSchema.from_dict(eligible_rates_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


