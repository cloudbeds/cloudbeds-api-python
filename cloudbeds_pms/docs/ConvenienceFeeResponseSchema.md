# ConvenienceFeeResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name (echoed) | 
**amount** | [**MoneySchema**](MoneySchema.md) |  | 
**rate** | **str** | Fee rate (echoed) | 
**rate_type** | **str** | How calculated (echoed) | 
**mode** | **str** | Mode used (echoed) | 

## Example

```python
from cloudbeds_pms.models.convenience_fee_response_schema import ConvenienceFeeResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConvenienceFeeResponseSchema from a JSON string
convenience_fee_response_schema_instance = ConvenienceFeeResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ConvenienceFeeResponseSchema.to_json())

# convert the object into a dict
convenience_fee_response_schema_dict = convenience_fee_response_schema_instance.to_dict()
# create an instance of ConvenienceFeeResponseSchema from a dict
convenience_fee_response_schema_from_dict = ConvenienceFeeResponseSchema.from_dict(convenience_fee_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


