# PostEmailTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**email_template_id** | **str** | The ID of the created email template. Only present if success &#x3D; true | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_email_template_response import PostEmailTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailTemplateResponse from a JSON string
post_email_template_response_instance = PostEmailTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PostEmailTemplateResponse.to_json())

# convert the object into a dict
post_email_template_response_dict = post_email_template_response_instance.to_dict()
# create an instance of PostEmailTemplateResponse from a dict
post_email_template_response_from_dict = PostEmailTemplateResponse.from_dict(post_email_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


