# FeeSchemaOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**fee_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.fee_schema_one_of import FeeSchemaOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of FeeSchemaOneOf from a JSON string
fee_schema_one_of_instance = FeeSchemaOneOf.from_json(json)
# print the JSON string representation of the object
print(FeeSchemaOneOf.to_json())

# convert the object into a dict
fee_schema_one_of_dict = fee_schema_one_of_instance.to_dict()
# create an instance of FeeSchemaOneOf from a dict
fee_schema_one_of_from_dict = FeeSchemaOneOf.from_dict(fee_schema_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


