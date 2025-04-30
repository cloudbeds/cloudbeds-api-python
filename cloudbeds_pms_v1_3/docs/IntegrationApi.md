# cloudbeds_pms_v1_3.IntegrationApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook_delete**](IntegrationApi.md#delete_webhook_delete) | **DELETE** /deleteWebhook | deleteWebhook
[**get_app_settings_get**](IntegrationApi.md#get_app_settings_get) | **GET** /getAppSettings | getAppSettings
[**get_app_state_get**](IntegrationApi.md#get_app_state_get) | **GET** /getAppState | getAppState
[**get_webhooks_get**](IntegrationApi.md#get_webhooks_get) | **GET** /getWebhooks | getWebhooks
[**post_app_error_post**](IntegrationApi.md#post_app_error_post) | **POST** /postAppError | postAppError
[**post_app_settings_post**](IntegrationApi.md#post_app_settings_post) | **POST** /postAppSettings | postAppSettings
[**post_app_state_internal_post**](IntegrationApi.md#post_app_state_internal_post) | **POST** /postAppStateInternal | postAppStateInternal
[**post_app_state_post**](IntegrationApi.md#post_app_state_post) | **POST** /postAppState | postAppState
[**post_government_receipt_post**](IntegrationApi.md#post_government_receipt_post) | **POST** /postGovernmentReceipt | postGovernmentReceipt
[**post_webhook_post**](IntegrationApi.md#post_webhook_post) | **POST** /postWebhook | postWebhook


# **delete_webhook_delete**
> DeleteWebhookResponse delete_webhook_delete(subscription_id, property_ids=property_ids)

deleteWebhook

Remove subscription for webhook. Read the [Webhooks guide](https://integrations.cloudbeds.com/hc/en-us/articles/360007612553-Webhooks) to see available objects, actions, payload info and more. ### Group account support

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_webhook_response import DeleteWebhookResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)

    try:
        # deleteWebhook
        api_response = api_instance.delete_webhook_delete(subscription_id, property_ids=property_ids)
        print("The response of IntegrationApi->delete_webhook_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->delete_webhook_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 

### Return type

[**DeleteWebhookResponse**](DeleteWebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_settings_get**
> GetAppSettingsResponse get_app_settings_get(property_id=property_id)

getAppSettings

Get the current app settings for a property.<br />

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_app_settings_response import GetAppSettingsResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be queried (optional)

    try:
        # getAppSettings
        api_response = api_instance.get_app_settings_get(property_id=property_id)
        print("The response of IntegrationApi->get_app_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->get_app_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be queried | [optional] 

### Return type

[**GetAppSettingsResponse**](GetAppSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_state_get**
> GetAppStateResponse get_app_state_get(property_id=property_id, client_id=client_id)

getAppState

Get the current app integration state for a property.<br /> This call is only available for internal usage. Read the [Connecting/Disconnecting Apps guide](https://integrations.cloudbeds.com/hc/en-us/articles/360007613213-Connecting-Disconnecting-Apps) to further understand the use cases.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_app_state_response import GetAppStateResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be queried (optional)
    client_id = 'client_id_example' # str | Client identifier (optional)

    try:
        # getAppState
        api_response = api_instance.get_app_state_get(property_id=property_id, client_id=client_id)
        print("The response of IntegrationApi->get_app_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->get_app_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be queried | [optional] 
 **client_id** | **str**| Client identifier | [optional] 

### Return type

[**GetAppStateResponse**](GetAppStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks_get**
> GetWebhooksResponse get_webhooks_get(property_id=property_id)

getWebhooks

List webhooks for which the API client is subscribed to.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_webhooks_response import GetWebhooksResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getWebhooks
        api_response = api_instance.get_webhooks_get(property_id=property_id)
        print("The response of IntegrationApi->get_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->get_webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetWebhooksResponse**](GetWebhooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_app_error_post**
> PostAppErrorResponse post_app_error_post(property_id=property_id, timestamp=timestamp, event_type=event_type, status_code=status_code, description=description, error_message=error_message, entity_type=entity_type, entity_id=entity_id, user_id=user_id)

postAppError

Submit the error received by the hybrid integration from the partner to the MFD

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_app_error_response import PostAppErrorResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
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
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be queried (optional)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime | Date/time that the error was received by the middleware (optional)
    event_type = 'event_type_example' # str | Description for the type of event that caused the error (optional)
    status_code = 'status_code_example' # str | HTTP error status code or other error code ID (optional)
    description = 'description_example' # str | Description of the error (optional)
    error_message = 'error_message_example' # str | Detailed message for error (optional)
    entity_type = 'entity_type_example' # str | Type of the entity related to the error (optional)
    entity_id = 'entity_id_example' # str | Unique ID for the entity related to the error (optional)
    user_id = 'user_id_example' # str | User ID for the user that triggered event that caused the error (optional)

    try:
        # postAppError
        api_response = api_instance.post_app_error_post(property_id=property_id, timestamp=timestamp, event_type=event_type, status_code=status_code, description=description, error_message=error_message, entity_type=entity_type, entity_id=entity_id, user_id=user_id)
        print("The response of IntegrationApi->post_app_error_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_app_error_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be queried | [optional] 
 **timestamp** | **datetime**| Date/time that the error was received by the middleware | [optional] 
 **event_type** | **str**| Description for the type of event that caused the error | [optional] 
 **status_code** | **str**| HTTP error status code or other error code ID | [optional] 
 **description** | **str**| Description of the error | [optional] 
 **error_message** | **str**| Detailed message for error | [optional] 
 **entity_type** | **str**| Type of the entity related to the error | [optional] 
 **entity_id** | **str**| Unique ID for the entity related to the error | [optional] 
 **user_id** | **str**| User ID for the user that triggered event that caused the error | [optional] 

### Return type

[**PostAppErrorResponse**](PostAppErrorResponse.md)

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

# **post_app_settings_post**
> PostAppSettingsResponse post_app_settings_post(property_id=property_id, settings=settings)

postAppSettings

Update the current app settings for a property.<br />

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_app_settings_request_settings_inner import PostAppSettingsRequestSettingsInner
from cloudbeds_pms_v1_3.models.post_app_settings_response import PostAppSettingsResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be queried (optional)
    settings = [cloudbeds_pms_v1_3.PostAppSettingsRequestSettingsInner()] # List[PostAppSettingsRequestSettingsInner] | An array of setings (optional)

    try:
        # postAppSettings
        api_response = api_instance.post_app_settings_post(property_id=property_id, settings=settings)
        print("The response of IntegrationApi->post_app_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_app_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be queried | [optional] 
 **settings** | [**List[PostAppSettingsRequestSettingsInner]**](PostAppSettingsRequestSettingsInner.md)| An array of setings | [optional] 

### Return type

[**PostAppSettingsResponse**](PostAppSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_app_state_internal_post**
> PostAppStateInternalResponse post_app_state_internal_post(property_id=property_id, client_id=client_id, app_state=app_state)

postAppStateInternal

Update app integration state for a property ID. <br /> This call is only available for internal usage. <br /> If an app is set to 'disabled', it will remove all active sessions Read the [Connecting/Disconnecting Apps guide](https://integrations.cloudbeds.com/hc/en-us/articles/360007613213-Connecting-Disconnecting-Apps) to further understand the use cases.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_app_state_internal_response import PostAppStateInternalResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be updated (optional)
    client_id = 'client_id_example' # str | Client identifier (optional)
    app_state = 'app_state_example' # str | Current integration state between third-party and property. (optional)

    try:
        # postAppStateInternal
        api_response = api_instance.post_app_state_internal_post(property_id=property_id, client_id=client_id, app_state=app_state)
        print("The response of IntegrationApi->post_app_state_internal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_app_state_internal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be updated | [optional] 
 **client_id** | **str**| Client identifier | [optional] 
 **app_state** | **str**| Current integration state between third-party and property. | [optional] 

### Return type

[**PostAppStateInternalResponse**](PostAppStateInternalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_app_state_post**
> PostAppStateResponse post_app_state_post(property_id=property_id, app_state=app_state)

postAppState

Update app integration state for a property ID. <br /> This call is only available for third-party integration partners, and not for property client IDs. <br /> If an app is set to 'disabled', it will remove all active sessions Read the [Connecting/Disconnecting Apps guide](https://integrations.cloudbeds.com/hc/en-us/articles/360007613213-Connecting-Disconnecting-Apps) to further understand the use cases.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_app_state_response import PostAppStateResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be updated (optional)
    app_state = 'app_state_example' # str | Current integration state between third-party and property. (optional)

    try:
        # postAppState
        api_response = api_instance.post_app_state_post(property_id=property_id, app_state=app_state)
        print("The response of IntegrationApi->post_app_state_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_app_state_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be updated | [optional] 
 **app_state** | **str**| Current integration state between third-party and property. | [optional] 

### Return type

[**PostAppStateResponse**](PostAppStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_government_receipt_post**
> PostGovernmentReceiptResponse post_government_receipt_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, name=name, url=url, amount=amount, identifier=identifier, issue_date=issue_date)

postGovernmentReceipt

Add a Government Receipt to a Reservation or House Account

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_government_receipt_response import PostGovernmentReceiptResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property identifier to be updated (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier. It, or houseAccountID, is necessary. (optional)
    house_account_id = 'house_account_id_example' # str | House Account identifier. It, or reservationID, is necessary. (optional)
    name = 'name_example' # str | Name of the document. Will be used to describe document in MFD. (optional)
    url = 'url_example' # str | URL for user to download document. (optional)
    amount = 3.4 # float | Value of posted document (optional)
    identifier = 'identifier_example' # str | Receipt Identifier of document. If not sent, a random identifier will be generated. (optional)
    issue_date = '2013-10-20T19:20:30+01:00' # datetime | Datetime of document emission, if not sent, current datetime will be assumed. (optional)

    try:
        # postGovernmentReceipt
        api_response = api_instance.post_government_receipt_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, name=name, url=url, amount=amount, identifier=identifier, issue_date=issue_date)
        print("The response of IntegrationApi->post_government_receipt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_government_receipt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property identifier to be updated | [optional] 
 **reservation_id** | **str**| Reservation identifier. It, or houseAccountID, is necessary. | [optional] 
 **house_account_id** | **str**| House Account identifier. It, or reservationID, is necessary. | [optional] 
 **name** | **str**| Name of the document. Will be used to describe document in MFD. | [optional] 
 **url** | **str**| URL for user to download document. | [optional] 
 **amount** | **float**| Value of posted document | [optional] 
 **identifier** | **str**| Receipt Identifier of document. If not sent, a random identifier will be generated. | [optional] 
 **issue_date** | **datetime**| Datetime of document emission, if not sent, current datetime will be assumed. | [optional] 

### Return type

[**PostGovernmentReceiptResponse**](PostGovernmentReceiptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook_post**
> PostWebhookResponse post_webhook_post(property_id=property_id, object=object, action=action, endpoint_url=endpoint_url)

postWebhook

Subscribe a webhook for a specified event. Read the [Webhooks guide](https://integrations.cloudbeds.com/hc/en-us/articles/360007612553-Webhooks) to see available objects, actions, payload info and more.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_webhook_response import PostWebhookResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.IntegrationApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    object = 'object_example' # str | Event object (optional)
    action = 'action_example' # str | Event action (optional)
    endpoint_url = 'endpoint_url_example' # str | Endpoint URL (optional)

    try:
        # postWebhook
        api_response = api_instance.post_webhook_post(property_id=property_id, object=object, action=action, endpoint_url=endpoint_url)
        print("The response of IntegrationApi->post_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->post_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **object** | **str**| Event object | [optional] 
 **action** | **str**| Event action | [optional] 
 **endpoint_url** | **str**| Endpoint URL | [optional] 

### Return type

[**PostWebhookResponse**](PostWebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

