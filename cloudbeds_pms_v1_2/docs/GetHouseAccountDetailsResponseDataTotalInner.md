# GetHouseAccountDetailsResponseDataTotalInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of House Account records | [optional] 
**quantity** | **str** | Total items quantity of product type records | [optional] 
**debit** | **str** | Total debit (formatted) | [optional] 
**credit** | **str** | Total credit (formatted) | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_house_account_details_response_data_total_inner import GetHouseAccountDetailsResponseDataTotalInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountDetailsResponseDataTotalInner from a JSON string
get_house_account_details_response_data_total_inner_instance = GetHouseAccountDetailsResponseDataTotalInner.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountDetailsResponseDataTotalInner.to_json())

# convert the object into a dict
get_house_account_details_response_data_total_inner_dict = get_house_account_details_response_data_total_inner_instance.to_dict()
# create an instance of GetHouseAccountDetailsResponseDataTotalInner from a dict
get_house_account_details_response_data_total_inner_from_dict = GetHouseAccountDetailsResponseDataTotalInner.from_dict(get_house_account_details_response_data_total_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


