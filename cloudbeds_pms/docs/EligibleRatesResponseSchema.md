# EligibleRatesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return. | 
**offset** | **int** | The offset for the current page of results. | 
**data** | [**List[EligibleRateItemSchema]**](EligibleRateItemSchema.md) | Eligible rates for exception creation (rate plans and base rates combined). | 

## Example

```python
from cloudbeds_pms.models.eligible_rates_response_schema import EligibleRatesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleRatesResponseSchema from a JSON string
eligible_rates_response_schema_instance = EligibleRatesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EligibleRatesResponseSchema.to_json())

# convert the object into a dict
eligible_rates_response_schema_dict = eligible_rates_response_schema_instance.to_dict()
# create an instance of EligibleRatesResponseSchema from a dict
eligible_rates_response_schema_from_dict = EligibleRatesResponseSchema.from_dict(eligible_rates_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


