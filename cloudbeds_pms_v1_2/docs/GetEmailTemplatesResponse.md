# GetEmailTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetEmailTemplatesResponseDataInner]**](GetEmailTemplatesResponseDataInner.md) | List of existing email templates | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_email_templates_response import GetEmailTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplatesResponse from a JSON string
get_email_templates_response_instance = GetEmailTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplatesResponse.to_json())

# convert the object into a dict
get_email_templates_response_dict = get_email_templates_response_instance.to_dict()
# create an instance of GetEmailTemplatesResponse from a dict
get_email_templates_response_from_dict = GetEmailTemplatesResponse.from_dict(get_email_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


