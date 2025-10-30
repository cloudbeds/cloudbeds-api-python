# cloudbeds_pms.DoorLocksApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**door_lock_key_controller_batch_delete**](DoorLocksApi.md#door_lock_key_controller_batch_delete) | **DELETE** /doorlock/v1/keys | Delete a list of doorlock keys.
[**door_lock_key_controller_create**](DoorLocksApi.md#door_lock_key_controller_create) | **POST** /doorlock/v1/keys | Create a new doorlock key.
[**door_lock_key_controller_delete**](DoorLocksApi.md#door_lock_key_controller_delete) | **DELETE** /doorlock/v1/keys/{id} | Delete a doorlock key.
[**door_lock_key_controller_index**](DoorLocksApi.md#door_lock_key_controller_index) | **GET** /doorlock/v1/keys/{propertyId} | Get a list of doorlock keys for a specific app client and property.
[**door_lock_key_controller_update**](DoorLocksApi.md#door_lock_key_controller_update) | **PATCH** /doorlock/v1/keys/{id} | Update a doorlock key.
[**door_lock_settings_controller_delete**](DoorLocksApi.md#door_lock_settings_controller_delete) | **DELETE** /doorlock/v1/settings/{propertyId} | Delete doorlock settings for property for specific application client.
[**door_lock_settings_controller_single**](DoorLocksApi.md#door_lock_settings_controller_single) | **GET** /doorlock/v1/settings/{propertyId} | Get doorlock settings for property for specific application client.
[**door_lock_settings_controller_upsert**](DoorLocksApi.md#door_lock_settings_controller_upsert) | **PUT** /doorlock/v1/settings/{propertyId} | Upsert doorlock settings for property for specific application client.


# **door_lock_key_controller_batch_delete**
> object door_lock_key_controller_batch_delete(key_ids, x_property_id)

Delete a list of doorlock keys.

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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    key_ids = '1,2' # str | 
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.

    try:
        # Delete a list of doorlock keys.
        api_response = api_instance.door_lock_key_controller_batch_delete(key_ids, x_property_id)
        print("The response of DoorLocksApi->door_lock_key_controller_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_key_controller_batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_ids** | **str**|  | 
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 

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
**204** | Keys were cancelled. |  -  |
**400** | Bad Request response |  -  |
**404** | Not found response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_key_controller_create**
> DoorLockKeyResponseSchema door_lock_key_controller_create(door_lock_key_create_request_schema)

Create a new doorlock key.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.door_lock_key_create_request_schema import DoorLockKeyCreateRequestSchema
from cloudbeds_pms.models.door_lock_key_response_schema import DoorLockKeyResponseSchema
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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    door_lock_key_create_request_schema = cloudbeds_pms.DoorLockKeyCreateRequestSchema() # DoorLockKeyCreateRequestSchema | Key data

    try:
        # Create a new doorlock key.
        api_response = api_instance.door_lock_key_controller_create(door_lock_key_create_request_schema)
        print("The response of DoorLocksApi->door_lock_key_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_key_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **door_lock_key_create_request_schema** | [**DoorLockKeyCreateRequestSchema**](DoorLockKeyCreateRequestSchema.md)| Key data | 

### Return type

[**DoorLockKeyResponseSchema**](DoorLockKeyResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A key that was just created. |  -  |
**400** | Bad Request response |  -  |
**404** | Not found response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_key_controller_delete**
> object door_lock_key_controller_delete(id, x_property_id)

Delete a doorlock key.

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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    id = 'id_example' # str | 
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.

    try:
        # Delete a doorlock key.
        api_response = api_instance.door_lock_key_controller_delete(id, x_property_id)
        print("The response of DoorLocksApi->door_lock_key_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_key_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 

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
**204** | A key that was just created. |  -  |
**400** | Bad Request response |  -  |
**404** | Not found response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_key_controller_index**
> DoorLockKeyListResponseSchema door_lock_key_controller_index(property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, key_ids=key_ids)

Get a list of doorlock keys for a specific app client and property.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.door_lock_key_list_response_schema import DoorLockKeyListResponseSchema
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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    property_id = 1 # int | The property ID
    reservation_id = cloudbeds_pms.ReservationId() # ReservationId |  (optional)
    sub_reservation_id = cloudbeds_pms.SubReservationId() # SubReservationId |  (optional)
    key_ids = '1,2,3' # str | Comma separated list of key ids (optional)

    try:
        # Get a list of doorlock keys for a specific app client and property.
        api_response = api_instance.door_lock_key_controller_index(property_id, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, key_ids=key_ids)
        print("The response of DoorLocksApi->door_lock_key_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_key_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **reservation_id** | **ReservationId**|  | [optional] 
 **sub_reservation_id** | **SubReservationId**|  | [optional] 
 **key_ids** | **str**| Comma separated list of key ids | [optional] 

### Return type

[**DoorLockKeyListResponseSchema**](DoorLockKeyListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of door lock keys. |  -  |
**400** | Bad Request response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **door_lock_key_controller_update**
> DoorLockKeyResponseSchema door_lock_key_controller_update(id, x_property_id, door_lock_key_update_request_schema)

Update a doorlock key.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.door_lock_key_response_schema import DoorLockKeyResponseSchema
from cloudbeds_pms.models.door_lock_key_update_request_schema import DoorLockKeyUpdateRequestSchema
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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    id = 'id_example' # str | 
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    door_lock_key_update_request_schema = cloudbeds_pms.DoorLockKeyUpdateRequestSchema() # DoorLockKeyUpdateRequestSchema | Key data

    try:
        # Update a doorlock key.
        api_response = api_instance.door_lock_key_controller_update(id, x_property_id, door_lock_key_update_request_schema)
        print("The response of DoorLocksApi->door_lock_key_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_key_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **door_lock_key_update_request_schema** | [**DoorLockKeyUpdateRequestSchema**](DoorLockKeyUpdateRequestSchema.md)| Key data | 

### Return type

[**DoorLockKeyResponseSchema**](DoorLockKeyResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated key. |  -  |
**400** | Bad Request response |  -  |
**404** | Not found response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    property_id = 1 # int | The property ID

    try:
        # Delete doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_delete(property_id)
        print("The response of DoorLocksApi->door_lock_settings_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_settings_controller_delete: %s\n" % e)
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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    property_id = 1 # int | The property ID

    try:
        # Get doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_single(property_id)
        print("The response of DoorLocksApi->door_lock_settings_controller_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_settings_controller_single: %s\n" % e)
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
    api_instance = cloudbeds_pms.DoorLocksApi(api_client)
    property_id = 1 # int | The property ID
    door_lock_settings_create_request_schema = cloudbeds_pms.DoorLockSettingsCreateRequestSchema() # DoorLockSettingsCreateRequestSchema | Settings data

    try:
        # Upsert doorlock settings for property for specific application client.
        api_response = api_instance.door_lock_settings_controller_upsert(property_id, door_lock_settings_create_request_schema)
        print("The response of DoorLocksApi->door_lock_settings_controller_upsert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoorLocksApi->door_lock_settings_controller_upsert: %s\n" % e)
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

