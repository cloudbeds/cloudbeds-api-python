# cloudbeds_pms_v1_2.EmailsApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_schedule_get**](EmailsApi.md#get_email_schedule_get) | **GET** /getEmailSchedule | getEmailSchedule
[**get_email_templates_get**](EmailsApi.md#get_email_templates_get) | **GET** /getEmailTemplates | getEmailTemplates
[**post_email_schedule_post**](EmailsApi.md#post_email_schedule_post) | **POST** /postEmailSchedule | postEmailSchedule
[**post_email_template_post**](EmailsApi.md#post_email_template_post) | **POST** /postEmailTemplate | postEmailTemplate


# **get_email_schedule_get**
> GetEmailScheduleResponse get_email_schedule_get(property_id=property_id)

getEmailSchedule

Returns a list of all existing email scheduling. This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_email_schedule_response import GetEmailScheduleResponse
from cloudbeds_pms_v1_2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.2
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_2.Configuration(
    host = "https://api.cloudbeds.com/api/v1.2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudbeds_pms_v1_2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_2.EmailsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getEmailSchedule
        api_response = api_instance.get_email_schedule_get(property_id=property_id)
        print("The response of EmailsApi->get_email_schedule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->get_email_schedule_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetEmailScheduleResponse**](GetEmailScheduleResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_templates_get**
> GetEmailTemplatesResponse get_email_templates_get(property_id=property_id)

getEmailTemplates

Returns a list of all existing email templates. This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_email_templates_response import GetEmailTemplatesResponse
from cloudbeds_pms_v1_2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.2
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_2.Configuration(
    host = "https://api.cloudbeds.com/api/v1.2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudbeds_pms_v1_2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_2.EmailsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getEmailTemplates
        api_response = api_instance.get_email_templates_get(property_id=property_id)
        print("The response of EmailsApi->get_email_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->get_email_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetEmailTemplatesResponse**](GetEmailTemplatesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_email_schedule_post**
> PostEmailScheduleResponse post_email_schedule_post(property_id=property_id, email_template_id=email_template_id, schedule_name=schedule_name, schedule=schedule)

postEmailSchedule

Creates a new email schedule for existing email template. Email template can be scheduled based on two parameters: reservationStatusChange and reservationEvent. Only one of the parameters can be used. *reservationStatusChange* schedules email to be sent when reservation status transitions to a specific one, for instance: `confirmed`. *reservationEvent* schedules email to be sent number of days prior or after a specific event, for instance: `after_check_out` at a given time This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_email_schedule_request_schedule import PostEmailScheduleRequestSchedule
from cloudbeds_pms_v1_2.models.post_email_schedule_response import PostEmailScheduleResponse
from cloudbeds_pms_v1_2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.2
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_2.Configuration(
    host = "https://api.cloudbeds.com/api/v1.2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudbeds_pms_v1_2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_2.EmailsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    email_template_id = 'email_template_id_example' # str | ID of the email template that will be used when sending an email. (optional)
    schedule_name = 'schedule_name_example' # str | User friendly schedule name that appears in the list. Should contain app name. (optional)
    schedule = cloudbeds_pms_v1_2.PostEmailScheduleRequestSchedule() # PostEmailScheduleRequestSchedule |  (optional)

    try:
        # postEmailSchedule
        api_response = api_instance.post_email_schedule_post(property_id=property_id, email_template_id=email_template_id, schedule_name=schedule_name, schedule=schedule)
        print("The response of EmailsApi->post_email_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->post_email_schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **email_template_id** | **str**| ID of the email template that will be used when sending an email. | [optional] 
 **schedule_name** | **str**| User friendly schedule name that appears in the list. Should contain app name. | [optional] 
 **schedule** | [**PostEmailScheduleRequestSchedule**](PostEmailScheduleRequestSchedule.md)|  | [optional] 

### Return type

[**PostEmailScheduleResponse**](PostEmailScheduleResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_email_template_post**
> PostEmailTemplateResponse post_email_template_post(property_id=property_id, email_type=email_type, name=name, var_from=var_from, from_name=from_name, subject=subject, body=body, reply_to=reply_to, reply_to_name=reply_to_name, autofill_all_languages=autofill_all_languages, cc=cc, bcc=bcc)

postEmailTemplate

Creates a new email template. See the full list of available language parameters <a href=\"https://integrations.cloudbeds.com/hc/en-us/articles/360007144993-FAQ#methods-and-parameters\">here</a>. This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_email_template_request_body import PostEmailTemplateRequestBody
from cloudbeds_pms_v1_2.models.post_email_template_request_subject import PostEmailTemplateRequestSubject
from cloudbeds_pms_v1_2.models.post_email_template_response import PostEmailTemplateResponse
from cloudbeds_pms_v1_2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.2
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_2.Configuration(
    host = "https://api.cloudbeds.com/api/v1.2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudbeds_pms_v1_2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_2.EmailsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    email_type = nonMarketing # str | Type of the email template: Marketing or Non-Marketing. Only applicable to GDPR-compliant properties. (optional) (default to nonMarketing)
    name = 'name_example' # str | Template name (optional)
    var_from = 'var_from_example' # str | Email address from which the email message may be sent (optional)
    from_name = 'from_name_example' # str | from which the email message may be sent. If empty email will be used (optional)
    subject = cloudbeds_pms_v1_2.PostEmailTemplateRequestSubject() # PostEmailTemplateRequestSubject |  (optional)
    body = cloudbeds_pms_v1_2.PostEmailTemplateRequestBody() # PostEmailTemplateRequestBody |  (optional)
    reply_to = 'reply_to_example' # str | Email address to which the email message may be replied. If empty, the value on from parameter will be used. (optional)
    reply_to_name = 'reply_to_name_example' # str | Name to which the email message may be replied. If empty, email will be used. (optional)
    autofill_all_languages = True # bool | If set, all languages will be set with the value for the property language. If not informed and only one language is sent, it's considered true, if more than one language is sent, it'll be considered false. (optional)
    cc = 'cc_example' # str | Email address to which the email message may be sent as a Carbon Copy (optional)
    bcc = 'bcc_example' # str | Email address to which the email message may be sent as a Blind Carbon Copy (optional)

    try:
        # postEmailTemplate
        api_response = api_instance.post_email_template_post(property_id=property_id, email_type=email_type, name=name, var_from=var_from, from_name=from_name, subject=subject, body=body, reply_to=reply_to, reply_to_name=reply_to_name, autofill_all_languages=autofill_all_languages, cc=cc, bcc=bcc)
        print("The response of EmailsApi->post_email_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->post_email_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **email_type** | **str**| Type of the email template: Marketing or Non-Marketing. Only applicable to GDPR-compliant properties. | [optional] [default to nonMarketing]
 **name** | **str**| Template name | [optional] 
 **var_from** | **str**| Email address from which the email message may be sent | [optional] 
 **from_name** | **str**| from which the email message may be sent. If empty email will be used | [optional] 
 **subject** | [**PostEmailTemplateRequestSubject**](PostEmailTemplateRequestSubject.md)|  | [optional] 
 **body** | [**PostEmailTemplateRequestBody**](PostEmailTemplateRequestBody.md)|  | [optional] 
 **reply_to** | **str**| Email address to which the email message may be replied. If empty, the value on from parameter will be used. | [optional] 
 **reply_to_name** | **str**| Name to which the email message may be replied. If empty, email will be used. | [optional] 
 **autofill_all_languages** | **bool**| If set, all languages will be set with the value for the property language. If not informed and only one language is sent, it&#39;s considered true, if more than one language is sent, it&#39;ll be considered false. | [optional] 
 **cc** | **str**| Email address to which the email message may be sent as a Carbon Copy | [optional] 
 **bcc** | **str**| Email address to which the email message may be sent as a Blind Carbon Copy | [optional] 

### Return type

[**PostEmailTemplateResponse**](PostEmailTemplateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

