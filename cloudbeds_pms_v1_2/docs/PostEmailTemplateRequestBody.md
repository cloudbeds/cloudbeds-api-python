# PostEmailTemplateRequestBody

Email message body. The body key should be a language code (IETF). A few examples are listed below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**en** | **str** | Email message body in English | [optional] 
**es** | **str** | Email message body in Spanish | [optional] 
**ru** | **str** | Email message body in Russian | [optional] 
**pt_br** | **str** | Email message body in Portuguese | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_email_template_request_body import PostEmailTemplateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailTemplateRequestBody from a JSON string
post_email_template_request_body_instance = PostEmailTemplateRequestBody.from_json(json)
# print the JSON string representation of the object
print(PostEmailTemplateRequestBody.to_json())

# convert the object into a dict
post_email_template_request_body_dict = post_email_template_request_body_instance.to_dict()
# create an instance of PostEmailTemplateRequestBody from a dict
post_email_template_request_body_from_dict = PostEmailTemplateRequestBody.from_dict(post_email_template_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


