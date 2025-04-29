# GetRoomsFeesAndTaxesResponseDataFeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_name** | **str** | Name of the fee | [optional] 
**fee_value** | **float** | Value of the fee for the selected parameters | [optional] 
**total_fees** | **float** | Total value of the fees | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rooms_fees_and_taxes_response_data_fees_inner import GetRoomsFeesAndTaxesResponseDataFeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsFeesAndTaxesResponseDataFeesInner from a JSON string
get_rooms_fees_and_taxes_response_data_fees_inner_instance = GetRoomsFeesAndTaxesResponseDataFeesInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomsFeesAndTaxesResponseDataFeesInner.to_json())

# convert the object into a dict
get_rooms_fees_and_taxes_response_data_fees_inner_dict = get_rooms_fees_and_taxes_response_data_fees_inner_instance.to_dict()
# create an instance of GetRoomsFeesAndTaxesResponseDataFeesInner from a dict
get_rooms_fees_and_taxes_response_data_fees_inner_from_dict = GetRoomsFeesAndTaxesResponseDataFeesInner.from_dict(get_rooms_fees_and_taxes_response_data_fees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


