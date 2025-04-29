# GetTaxesAndFeesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 
**data** | [**List[GetTaxesAndFeesResponseDataInner]**](GetTaxesAndFeesResponseDataInner.md) | Details for the taxes and fees. If success &#x3D; false, it may not exist. | [optional] 
**total** | **int** | Total number of results | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response import GetTaxesAndFeesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponse from a JSON string
get_taxes_and_fees_response_instance = GetTaxesAndFeesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponse.to_json())

# convert the object into a dict
get_taxes_and_fees_response_dict = get_taxes_and_fees_response_instance.to_dict()
# create an instance of GetTaxesAndFeesResponse from a dict
get_taxes_and_fees_response_from_dict = GetTaxesAndFeesResponse.from_dict(get_taxes_and_fees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


