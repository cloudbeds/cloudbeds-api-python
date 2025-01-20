# cloudbeds_pms.DoorlockSettingsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**door_lock_settings_controller_delete**](DoorlockSettingsApi.md#door_lock_settings_controller_delete) | **DELETE** /doorlock/v1/settings/{propertyId} | Delete doorlock settings for property for specific application client.
[**door_lock_settings_controller_single**](DoorlockSettingsApi.md#door_lock_settings_controller_single) | **GET** /doorlock/v1/settings/{propertyId} | Get doorlock settings for property for specific application client.
[**door_lock_settings_controller_upsert**](DoorlockSettingsApi.md#door_lock_settings_controller_upsert) | **PUT** /doorlock/v1/settings/{propertyId} | Upsert doorlock settings for property for specific application client.


# **door_lock_settings_controller_delete**
> object door_lock_settings_controller_delete(property_id)

Delete doorlock settings for property for specific application client.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.DoorlockSettingsApi(api_client)
    property_id = 1 # int | The property ID

    try:
        # Delete doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_delete(property_id)
        print("The response of DoorlockSettingsApi->door_lock_settings_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorlockSettingsApi->door_lock_settings_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response on successful delete |  -  |
**400** | Bad Request response |  -  |
**404** | Not Found response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_settings_controller_single**
> DoorLockSettingsResponseSchema door_lock_settings_controller_single(property_id)

Get doorlock settings for property for specific application client.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.door_lock_settings_response_schema import DoorLockSettingsResponseSchema
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.DoorlockSettingsApi(api_client)
    property_id = 1 # int | The property ID

    try:
        # Get doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_single(property_id)
        print("The response of DoorlockSettingsApi->door_lock_settings_controller_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorlockSettingsApi->door_lock_settings_controller_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 

### Return type

[**DoorLockSettingsResponseSchema**](DoorLockSettingsResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Doorlock settings for property for specific application client. |  -  |
**400** | Bad Request response |  -  |
**404** | Not Found response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_settings_controller_upsert**
> object door_lock_settings_controller_upsert(property_id, door_lock_settings_create_request_schema)

Upsert doorlock settings for property for specific application client.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.door_lock_settings_create_request_schema import DoorLockSettingsCreateRequestSchema
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.DoorlockSettingsApi(api_client)
    property_id = 1 # int | The property ID
    door_lock_settings_create_request_schema = cloudbeds_pms.DoorLockSettingsCreateRequestSchema() # DoorLockSettingsCreateRequestSchema | Settings data

    try:
        # Upsert doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_upsert(property_id, door_lock_settings_create_request_schema)
        print("The response of DoorlockSettingsApi->door_lock_settings_controller_upsert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorlockSettingsApi->door_lock_settings_controller_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **door_lock_settings_create_request_schema** | [**DoorLockSettingsCreateRequestSchema**](DoorLockSettingsCreateRequestSchema.md)| Settings data | 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response on successful create |  -  |
**400** | Bad Request response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

