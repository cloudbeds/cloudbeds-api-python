# ConvenienceFeeConfigSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the surcharge | 
**rate** | **str** | Fee rate in minor units. For percentage: the rate in minor units (e.g., \&quot;300\&quot; &#x3D; 3.00%). | 
**rate_type** | **str** | How the fee is calculated | 
**mode** | **str** | Calculation mode. fee_on_top &#x3D; added to total. fee_from_total &#x3D; extracted from total. | 

## Example

```python
from cloudbeds_pms.models.convenience_fee_config_schema import ConvenienceFeeConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConvenienceFeeConfigSchema from a JSON string
convenience_fee_config_schema_instance = ConvenienceFeeConfigSchema.from_json(json)
# print the JSON string representation of the object
print(ConvenienceFeeConfigSchema.to_json())

# convert the object into a dict
convenience_fee_config_schema_dict = convenience_fee_config_schema_instance.to_dict()
# create an instance of ConvenienceFeeConfigSchema from a dict
convenience_fee_config_schema_from_dict = ConvenienceFeeConfigSchema.from_dict(convenience_fee_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


