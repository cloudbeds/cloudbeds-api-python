# GetSourcesResponseDataInnerTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | ID of tax | [optional] 
**name** | **str** | Name of tax | [optional] 
**amount** | **float** | Value of tax | [optional] 
**amount_type** | **str** | If tax is percentage of amount or fixed | [optional] 
**type** | **str** | If tax is included or not in final price | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_sources_response_data_inner_taxes_inner import GetSourcesResponseDataInnerTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSourcesResponseDataInnerTaxesInner from a JSON string
get_sources_response_data_inner_taxes_inner_instance = GetSourcesResponseDataInnerTaxesInner.from_json(json)
# print the JSON string representation of the object
print(GetSourcesResponseDataInnerTaxesInner.to_json())

# convert the object into a dict
get_sources_response_data_inner_taxes_inner_dict = get_sources_response_data_inner_taxes_inner_instance.to_dict()
# create an instance of GetSourcesResponseDataInnerTaxesInner from a dict
get_sources_response_data_inner_taxes_inner_from_dict = GetSourcesResponseDataInnerTaxesInner.from_dict(get_sources_response_data_inner_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


