# PostAppPropertySettingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**PostAppPropertySettingResponseData**](PostAppPropertySettingResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_app_property_setting_response import PostAppPropertySettingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAppPropertySettingResponse from a JSON string
post_app_property_setting_response_instance = PostAppPropertySettingResponse.from_json(json)
# print the JSON string representation of the object
print(PostAppPropertySettingResponse.to_json())

# convert the object into a dict
post_app_property_setting_response_dict = post_app_property_setting_response_instance.to_dict()
# create an instance of PostAppPropertySettingResponse from a dict
post_app_property_setting_response_from_dict = PostAppPropertySettingResponse.from_dict(post_app_property_setting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


