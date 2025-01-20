# PostEmailTemplateRequestSubject

Email message subject. The subject key should be a language code (IETF). A few examples are listed below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**en** | **str** | Email message subject in English | [optional] 
**es** | **str** | Email message subject in Spanish | [optional] 
**ru** | **str** | Email message subject in Russian | [optional] 
**pt_br** | **str** | Email message subject in Portuguese | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_email_template_request_subject import PostEmailTemplateRequestSubject

# TODO update the JSON string below
json = "{}"
# create an instance of PostEmailTemplateRequestSubject from a JSON string
post_email_template_request_subject_instance = PostEmailTemplateRequestSubject.from_json(json)
# print the JSON string representation of the object
print(PostEmailTemplateRequestSubject.to_json())

# convert the object into a dict
post_email_template_request_subject_dict = post_email_template_request_subject_instance.to_dict()
# create an instance of PostEmailTemplateRequestSubject from a dict
post_email_template_request_subject_from_dict = PostEmailTemplateRequestSubject.from_dict(post_email_template_request_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


