# PostNewHouseAccountResponseData

House Account details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**house_account_id** | **str** | Unique identifier of created House Account | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_new_house_account_response_data import PostNewHouseAccountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewHouseAccountResponseData from a JSON string
post_new_house_account_response_data_instance = PostNewHouseAccountResponseData.from_json(json)
# print the JSON string representation of the object
print(PostNewHouseAccountResponseData.to_json())

# convert the object into a dict
post_new_house_account_response_data_dict = post_new_house_account_response_data_instance.to_dict()
# create an instance of PostNewHouseAccountResponseData from a dict
post_new_house_account_response_data_from_dict = PostNewHouseAccountResponseData.from_dict(post_new_house_account_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


