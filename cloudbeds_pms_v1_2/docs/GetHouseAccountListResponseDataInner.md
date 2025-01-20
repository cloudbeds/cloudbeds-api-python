# GetHouseAccountListResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | House Account ID | [optional] 
**property_id** | **str** | Property ID | [optional] 
**account_name** | **str** | House Account name | [optional] 
**account_status** | **str** | House Account status | [optional] 
**is_private** | **bool** | Whether House Account is set to private or not (if true \&quot;userName\&quot; will be specified) | [optional] 
**user_name** | **str** | Owner Name of private House Account | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_house_account_list_response_data_inner import GetHouseAccountListResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountListResponseDataInner from a JSON string
get_house_account_list_response_data_inner_instance = GetHouseAccountListResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountListResponseDataInner.to_json())

# convert the object into a dict
get_house_account_list_response_data_inner_dict = get_house_account_list_response_data_inner_instance.to_dict()
# create an instance of GetHouseAccountListResponseDataInner from a dict
get_house_account_list_response_data_inner_from_dict = GetHouseAccountListResponseDataInner.from_dict(get_house_account_list_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


