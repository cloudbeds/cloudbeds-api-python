# PostAppPropertySettingResponseData

Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_app_property_setting_response_data import PostAppPropertySettingResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppPropertySettingResponseData from a JSON string
post_app_property_setting_response_data_instance = PostAppPropertySettingResponseData.from_json(json)
# print the JSON string representation of the object
print(PostAppPropertySettingResponseData.to_json())

# convert the object into a dict
post_app_property_setting_response_data_dict = post_app_property_setting_response_data_instance.to_dict()
# create an instance of PostAppPropertySettingResponseData from a dict
post_app_property_setting_response_data_from_dict = PostAppPropertySettingResponseData.from_dict(post_app_property_setting_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


