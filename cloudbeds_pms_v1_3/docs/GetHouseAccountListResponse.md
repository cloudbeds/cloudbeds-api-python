# GetHouseAccountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetHouseAccountListResponseDataInner]**](GetHouseAccountListResponseDataInner.md) | Details for the house accounts | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_house_account_list_response import GetHouseAccountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountListResponse from a JSON string
get_house_account_list_response_instance = GetHouseAccountListResponse.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountListResponse.to_json())

# convert the object into a dict
get_house_account_list_response_dict = get_house_account_list_response_instance.to_dict()
# create an instance of GetHouseAccountListResponse from a dict
get_house_account_list_response_from_dict = GetHouseAccountListResponse.from_dict(get_house_account_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


