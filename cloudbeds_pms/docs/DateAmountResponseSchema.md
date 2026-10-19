# DateAmountResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date (YYYY-MM-DD). | 
**amount_allotted_for_sale** | **int** | Operator-set amount allotted for sale. | 

## Example

```python
from cloudbeds_pms.models.date_amount_response_schema import DateAmountResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DateAmountResponseSchema from a JSON string
date_amount_response_schema_instance = DateAmountResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DateAmountResponseSchema.to_json())

# convert the object into a dict
date_amount_response_schema_dict = date_amount_response_schema_instance.to_dict()
# create an instance of DateAmountResponseSchema from a dict
date_amount_response_schema_from_dict = DateAmountResponseSchema.from_dict(date_amount_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


