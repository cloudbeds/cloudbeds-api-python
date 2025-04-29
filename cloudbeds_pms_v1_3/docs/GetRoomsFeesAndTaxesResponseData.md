# GetRoomsFeesAndTaxesResponseData

Details of the fees and taxes applicable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**List[GetRoomsFeesAndTaxesResponseDataFeesInner]**](GetRoomsFeesAndTaxesResponseDataFeesInner.md) | Details of the fees applicable | [optional] 
**taxes** | [**List[GetRoomsFeesAndTaxesResponseDataTaxesInner]**](GetRoomsFeesAndTaxesResponseDataTaxesInner.md) | Details of the taxes applicable | [optional] 
**rooms_total_without_taxes** | **float** | \&quot;roomsTotal\&quot; parameter subtracting the included taxes | [optional] 
**grand_total** | **float** | Total with fees and taxes | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rooms_fees_and_taxes_response_data import GetRoomsFeesAndTaxesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsFeesAndTaxesResponseData from a JSON string
get_rooms_fees_and_taxes_response_data_instance = GetRoomsFeesAndTaxesResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRoomsFeesAndTaxesResponseData.to_json())

# convert the object into a dict
get_rooms_fees_and_taxes_response_data_dict = get_rooms_fees_and_taxes_response_data_instance.to_dict()
# create an instance of GetRoomsFeesAndTaxesResponseData from a dict
get_rooms_fees_and_taxes_response_data_from_dict = GetRoomsFeesAndTaxesResponseData.from_dict(get_rooms_fees_and_taxes_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


