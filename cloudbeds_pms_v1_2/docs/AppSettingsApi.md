# cloudbeds_pms_v1_2.AppSettingsApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_property_settings_post**](AppSettingsApi.md#delete_app_property_settings_post) | **POST** /deleteAppPropertySettings | deleteAppPropertySettings
[**get_app_property_settings_get**](AppSettingsApi.md#get_app_property_settings_get) | **GET** /getAppPropertySettings | getAppPropertySettings
[**post_app_property_settings_post**](AppSettingsApi.md#post_app_property_settings_post) | **POST** /postAppPropertySettings | postAppPropertySettings
[**put_app_property_settings_post**](AppSettingsApi.md#put_app_property_settings_post) | **POST** /putAppPropertySettings | putAppPropertySettings


# **delete_app_property_settings_post**
> PostDeleteAppPropertySettingsResponse delete_app_property_settings_post(property_id=property_id, key=key)

deleteAppPropertySettings



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_delete_app_property_settings_response import PostDeleteAppPropertySettingsResponse
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
    api_instance = cloudbeds_pms_v1_2.AppSettingsApi(api_client)
    property_id = 'property_id_example' # str | Key (optional)
    key = 'key_example' # str | Key (optional)

    try:
        # deleteAppPropertySettings
        api_response = api_instance.delete_app_property_settings_post(property_id=property_id, key=key)
        print("The response of AppSettingsApi->delete_app_property_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingsApi->delete_app_property_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Key | [optional] 
 **key** | **str**| Key | [optional] 

### Return type

[**PostDeleteAppPropertySettingsResponse**](PostDeleteAppPropertySettingsResponse.md)

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

# **get_app_property_settings_get**
> GetAppPropertySettingsResponse get_app_property_settings_get(property_id, key=key)

getAppPropertySettings

Returns the app property settings

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_app_property_settings_response import GetAppPropertySettingsResponse
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
    api_instance = cloudbeds_pms_v1_2.AppSettingsApi(api_client)
    property_id = 'property_id_example' # str | Property ID
    key = 'key_example' # str | Key (optional)

    try:
        # getAppPropertySettings
        api_response = api_instance.get_app_property_settings_get(property_id, key=key)
        print("The response of AppSettingsApi->get_app_property_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingsApi->get_app_property_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | 
 **key** | **str**| Key | [optional] 

### Return type

[**GetAppPropertySettingsResponse**](GetAppPropertySettingsResponse.md)

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

# **post_app_property_settings_post**
> PostAppPropertySettingResponse post_app_property_settings_post(property_id=property_id, app_client_id=app_client_id, key=key, value=value)

postAppPropertySettings



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_app_property_setting_response import PostAppPropertySettingResponse
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
    api_instance = cloudbeds_pms_v1_2.AppSettingsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    app_client_id = 'app_client_id_example' # str | Application Client ID (optional)
    key = 'key_example' # str | Key (optional)
    value = 'value_example' # str | Value (optional)

    try:
        # postAppPropertySettings
        api_response = api_instance.post_app_property_settings_post(property_id=property_id, app_client_id=app_client_id, key=key, value=value)
        print("The response of AppSettingsApi->post_app_property_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingsApi->post_app_property_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **app_client_id** | **str**| Application Client ID | [optional] 
 **key** | **str**| Key | [optional] 
 **value** | **str**| Value | [optional] 

### Return type

[**PostAppPropertySettingResponse**](PostAppPropertySettingResponse.md)

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

# **put_app_property_settings_post**
> PostPutAppPropertySettingsResponse put_app_property_settings_post(property_id=property_id, key=key, value=value)

putAppPropertySettings



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_put_app_property_settings_response import PostPutAppPropertySettingsResponse
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
    api_instance = cloudbeds_pms_v1_2.AppSettingsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    key = 'key_example' # str | Key (optional)
    value = 'value_example' # str | Value (optional)

    try:
        # putAppPropertySettings
        api_response = api_instance.put_app_property_settings_post(property_id=property_id, key=key, value=value)
        print("The response of AppSettingsApi->put_app_property_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppSettingsApi->put_app_property_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **key** | **str**| Key | [optional] 
 **value** | **str**| Value | [optional] 

### Return type

[**PostPutAppPropertySettingsResponse**](PostPutAppPropertySettingsResponse.md)

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

