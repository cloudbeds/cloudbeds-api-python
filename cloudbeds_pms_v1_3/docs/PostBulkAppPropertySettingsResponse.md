# PostBulkAppPropertySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_bulk_app_property_settings_response import PostBulkAppPropertySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostBulkAppPropertySettingsResponse from a JSON string
post_bulk_app_property_settings_response_instance = PostBulkAppPropertySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PostBulkAppPropertySettingsResponse.to_json())

# convert the object into a dict
post_bulk_app_property_settings_response_dict = post_bulk_app_property_settings_response_instance.to_dict()
# create an instance of PostBulkAppPropertySettingsResponse from a dict
post_bulk_app_property_settings_response_from_dict = PostBulkAppPropertySettingsResponse.from_dict(post_bulk_app_property_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


