# PostCustomFieldResponseData

Field details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Field name | [optional] 
**name** | **str** | Field name | [optional] 
**shortcode** | **str** | Internal reference and is used for integration purposes such as custom links and the API | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_custom_field_response_data import PostCustomFieldResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomFieldResponseData from a JSON string
post_custom_field_response_data_instance = PostCustomFieldResponseData.from_json(json)
# print the JSON string representation of the object
print(PostCustomFieldResponseData.to_json())

# convert the object into a dict
post_custom_field_response_data_dict = post_custom_field_response_data_instance.to_dict()
# create an instance of PostCustomFieldResponseData from a dict
post_custom_field_response_data_from_dict = PostCustomFieldResponseData.from_dict(post_custom_field_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


