# GetRoomsFeesAndTaxesResponseDataTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Name of the tax | [optional] 
**fee_value** | **str** | Value of the tax for the selected parameters | [optional] 
**total_taxes** | **float** | Total value of the taxes | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rooms_fees_and_taxes_response_data_taxes_inner import GetRoomsFeesAndTaxesResponseDataTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsFeesAndTaxesResponseDataTaxesInner from a JSON string
get_rooms_fees_and_taxes_response_data_taxes_inner_instance = GetRoomsFeesAndTaxesResponseDataTaxesInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomsFeesAndTaxesResponseDataTaxesInner.to_json())

# convert the object into a dict
get_rooms_fees_and_taxes_response_data_taxes_inner_dict = get_rooms_fees_and_taxes_response_data_taxes_inner_instance.to_dict()
# create an instance of GetRoomsFeesAndTaxesResponseDataTaxesInner from a dict
get_rooms_fees_and_taxes_response_data_taxes_inner_from_dict = GetRoomsFeesAndTaxesResponseDataTaxesInner.from_dict(get_rooms_fees_and_taxes_response_data_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


