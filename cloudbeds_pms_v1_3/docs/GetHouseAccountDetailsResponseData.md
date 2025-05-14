# GetHouseAccountDetailsResponseData

Includes records list for House Account and summary info covering the date range specified

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[GetHouseAccountDetailsResponseDataTotalInner]**](GetHouseAccountDetailsResponseDataTotalInner.md) | Section with summary records info | [optional] 
**records** | [**List[GetHouseAccountDetailsResponseDataRecordsInner]**](GetHouseAccountDetailsResponseDataRecordsInner.md) | Section with records list | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_house_account_details_response_data import GetHouseAccountDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountDetailsResponseData from a JSON string
get_house_account_details_response_data_instance = GetHouseAccountDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountDetailsResponseData.to_json())

# convert the object into a dict
get_house_account_details_response_data_dict = get_house_account_details_response_data_instance.to_dict()
# create an instance of GetHouseAccountDetailsResponseData from a dict
get_house_account_details_response_data_from_dict = GetHouseAccountDetailsResponseData.from_dict(get_house_account_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


