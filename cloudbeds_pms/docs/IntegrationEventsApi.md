# cloudbeds_pms.IntegrationEventsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_event_controller_create**](IntegrationEventsApi.md#integration_event_controller_create) | **POST** /integration/v1/events | Create a new integration event.
[**integration_event_controller_index**](IntegrationEventsApi.md#integration_event_controller_index) | **GET** /integration/v1/events | Get a list of integration events for a specific property.
[**integration_event_controller_retry**](IntegrationEventsApi.md#integration_event_controller_retry) | **POST** /integration/v1/events/{id}/retry | Retry an integration event.
[**integration_event_controller_update**](IntegrationEventsApi.md#integration_event_controller_update) | **PATCH** /integration/v1/events/{id} | Update an integration event.


# **integration_event_controller_create**
> IntegrationEventResponseSchema integration_event_controller_create(x_property_id, integration_event_create_request_schema)

Create a new integration event.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.integration_event_create_request_schema import IntegrationEventCreateRequestSchema
from cloudbeds_pms.models.integration_event_response_schema import IntegrationEventResponseSchema
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
    api_instance = cloudbeds_pms.IntegrationEventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    integration_event_create_request_schema = cloudbeds_pms.IntegrationEventCreateRequestSchema() # IntegrationEventCreateRequestSchema | Integration event data

    try:
        # Create a new integration event.
        api_response = api_instance.integration_event_controller_create(x_property_id, integration_event_create_request_schema)
        print("The response of IntegrationEventsApi->integration_event_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationEventsApi->integration_event_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **integration_event_create_request_schema** | [**IntegrationEventCreateRequestSchema**](IntegrationEventCreateRequestSchema.md)| Integration event data | 

### Return type

[**IntegrationEventResponseSchema**](IntegrationEventResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An integration event that was just created. |  -  |
**400** | Bad Request response |  -  |
**401** | Unauthorized response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_event_controller_index**
> IntegrationEventListResponseSchema integration_event_controller_index(x_property_id, sort=sort, limit=limit, offset=offset, filters=filters)

Get a list of integration events for a specific property.

### Example


```python
import cloudbeds_pms
from cloudbeds_pms.models.integration_event_list_response_schema import IntegrationEventListResponseSchema
from cloudbeds_pms.models.limit_offset_pagination_schema import LimitOffsetPaginationSchema
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema
from cloudbeds_pms.models.query_parameter_sort_schema import QueryParameterSortSchema
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)


# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.IntegrationEventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    sort = cloudbeds_pms.QueryParameterSortSchema() # QueryParameterSortSchema | A string specifying fields for sorting with optional directions (e.g., asc or desc). (optional)
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)
    filters = cloudbeds_pms.QueryParameterDynamicFilterSchema() # QueryParameterDynamicFilterSchema | This parameter should be formatted as a list of strings separated by ; (optional)

    try:
        # Get a list of integration events for a specific property.
        api_response = api_instance.integration_event_controller_index(x_property_id, sort=sort, limit=limit, offset=offset, filters=filters)
        print("The response of IntegrationEventsApi->integration_event_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationEventsApi->integration_event_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **sort** | [**QueryParameterSortSchema**](.md)| A string specifying fields for sorting with optional directions (e.g., asc or desc). | [optional] 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 
 **filters** | [**QueryParameterDynamicFilterSchema**](.md)| This parameter should be formatted as a list of strings separated by ; | [optional] 

### Return type

[**IntegrationEventListResponseSchema**](IntegrationEventListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of integration events. |  -  |
**400** | Bad Request response |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_event_controller_retry**
> object integration_event_controller_retry(id, x_property_id, integration_event_update_request_schema)

Retry an integration event.

### Example


```python
import cloudbeds_pms
from cloudbeds_pms.models.integration_event_update_request_schema import IntegrationEventUpdateRequestSchema
from cloudbeds_pms.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms.Configuration(
    host = "https://api.cloudbeds.com"
)


# Enter a context with an instance of the API client
with cloudbeds_pms.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms.IntegrationEventsApi(api_client)
    id = 'id_example' # str | 
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    integration_event_update_request_schema = cloudbeds_pms.IntegrationEventUpdateRequestSchema() # IntegrationEventUpdateRequestSchema | Integration event data

    try:
        # Retry an integration event.
        api_response = api_instance.integration_event_controller_retry(id, x_property_id, integration_event_update_request_schema)
        print("The response of IntegrationEventsApi->integration_event_controller_retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationEventsApi->integration_event_controller_retry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **integration_event_update_request_schema** | [**IntegrationEventUpdateRequestSchema**](IntegrationEventUpdateRequestSchema.md)| Integration event data | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A request was sent to initiate integration event retry. |  -  |
**400** | Bad Request response |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integration_event_controller_update**
> IntegrationEventResponseSchema integration_event_controller_update(id, x_property_id, integration_event_update_request_schema)

Update an integration event.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.integration_event_response_schema import IntegrationEventResponseSchema
from cloudbeds_pms.models.integration_event_update_request_schema import IntegrationEventUpdateRequestSchema
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
    api_instance = cloudbeds_pms.IntegrationEventsApi(api_client)
    id = 'id_example' # str | 
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    integration_event_update_request_schema = cloudbeds_pms.IntegrationEventUpdateRequestSchema() # IntegrationEventUpdateRequestSchema | Integration event data

    try:
        # Update an integration event.
        api_response = api_instance.integration_event_controller_update(id, x_property_id, integration_event_update_request_schema)
        print("The response of IntegrationEventsApi->integration_event_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationEventsApi->integration_event_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **integration_event_update_request_schema** | [**IntegrationEventUpdateRequestSchema**](IntegrationEventUpdateRequestSchema.md)| Integration event data | 

### Return type

[**IntegrationEventResponseSchema**](IntegrationEventResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An integration event that was just updated. |  -  |
**400** | Bad Request response |  -  |
**401** | Unauthorized response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

