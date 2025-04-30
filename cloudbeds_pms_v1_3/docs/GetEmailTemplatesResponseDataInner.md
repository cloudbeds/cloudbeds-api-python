# GetEmailTemplatesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_id** | **str** | ID of the email template | [optional] 
**name** | **str** | Name | [optional] 
**subject** | **str** | Subject | [optional] 
**is_active** | **bool** | True if email template is active; false if not | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_email_templates_response_data_inner import GetEmailTemplatesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplatesResponseDataInner from a JSON string
get_email_templates_response_data_inner_instance = GetEmailTemplatesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplatesResponseDataInner.to_json())

# convert the object into a dict
get_email_templates_response_data_inner_dict = get_email_templates_response_data_inner_instance.to_dict()
# create an instance of GetEmailTemplatesResponseDataInner from a dict
get_email_templates_response_data_inner_from_dict = GetEmailTemplatesResponseDataInner.from_dict(get_email_templates_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


