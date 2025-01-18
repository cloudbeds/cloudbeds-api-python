# GetHouseAccountDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetHouseAccountDetailsResponseData**](GetHouseAccountDetailsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_house_account_details_response import GetHouseAccountDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountDetailsResponse from a JSON string
get_house_account_details_response_instance = GetHouseAccountDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountDetailsResponse.to_json())

# convert the object into a dict
get_house_account_details_response_dict = get_house_account_details_response_instance.to_dict()
# create an instance of GetHouseAccountDetailsResponse from a dict
get_house_account_details_response_from_dict = GetHouseAccountDetailsResponse.from_dict(get_house_account_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


