# cloudbeds_pms.MarketSegmentationGroupsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_controller_create**](MarketSegmentationGroupsApi.md#group_controller_create) | **POST** /market-segmentation/v1/groups | Create a new Market Segmentation Group.
[**group_controller_delete**](MarketSegmentationGroupsApi.md#group_controller_delete) | **DELETE** /market-segmentation/v1/groups/{id} | Delete a Market Segmentation Group.
[**group_controller_disable**](MarketSegmentationGroupsApi.md#group_controller_disable) | **POST** /market-segmentation/v1/groups/{id}/disable | Disable a Market Segmentation Group.
[**group_controller_enable**](MarketSegmentationGroupsApi.md#group_controller_enable) | **POST** /market-segmentation/v1/groups/{id}/enable | Enable a Market Segmentation Group.
[**group_controller_index**](MarketSegmentationGroupsApi.md#group_controller_index) | **GET** /market-segmentation/v1/groups | Get a list of Market Segmentation Groups.
[**group_controller_single**](MarketSegmentationGroupsApi.md#group_controller_single) | **GET** /market-segmentation/v1/groups/{id} | Get Market Segmentation Group data.
[**group_controller_update**](MarketSegmentationGroupsApi.md#group_controller_update) | **PATCH** /market-segmentation/v1/groups/{id} | Update a Market Segmentation Group.


# **group_controller_create**
> GroupResponseSchema group_controller_create(x_property_id, group_create_request_schema)

Create a new Market Segmentation Group.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.group_create_request_schema import GroupCreateRequestSchema
from cloudbeds_pms.models.group_response_schema import GroupResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    group_create_request_schema = cloudbeds_pms.GroupCreateRequestSchema() # GroupCreateRequestSchema | Group data.

    try:
        # Create a new Market Segmentation Group.
        api_response = api_instance.group_controller_create(x_property_id, group_create_request_schema)
        print("The response of MarketSegmentationGroupsApi->group_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **group_create_request_schema** | [**GroupCreateRequestSchema**](GroupCreateRequestSchema.md)| Group data. | 

### Return type

[**GroupResponseSchema**](GroupResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Market Segmentation Group. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_delete**
> object group_controller_delete(x_property_id, id)

Delete a Market Segmentation Group.

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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Group ID.

    try:
        # Delete a Market Segmentation Group.
        api_response = api_instance.group_controller_delete(x_property_id, id)
        print("The response of MarketSegmentationGroupsApi->group_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Group ID. | 

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
**204** | Market Segmentation Group was deleted. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_disable**
> object group_controller_disable(x_property_id, id)

Disable a Market Segmentation Group.

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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Group ID.

    try:
        # Disable a Market Segmentation Group.
        api_response = api_instance.group_controller_disable(x_property_id, id)
        print("The response of MarketSegmentationGroupsApi->group_controller_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Group ID. | 

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
**204** | Market Segmentation Group was disabled. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_enable**
> object group_controller_enable(x_property_id, id)

Enable a Market Segmentation Group.

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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Group ID.

    try:
        # Enable a Market Segmentation Group.
        api_response = api_instance.group_controller_enable(x_property_id, id)
        print("The response of MarketSegmentationGroupsApi->group_controller_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Group ID. | 

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
**204** | Market Segmentation Group was enabled. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_index**
> GroupListResponseSchema group_controller_index(x_property_id, offset=offset, limit=limit)

Get a list of Market Segmentation Groups.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.group_list_response_schema import GroupListResponseSchema
from cloudbeds_pms.models.limit_offset_pagination_schema import LimitOffsetPaginationSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)

    try:
        # Get a list of Market Segmentation Groups.
        api_response = api_instance.group_controller_index(x_property_id, offset=offset, limit=limit)
        print("The response of MarketSegmentationGroupsApi->group_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 

### Return type

[**GroupListResponseSchema**](GroupListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Market Segmentation Groups. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_single**
> GroupResponseSchema group_controller_single(x_property_id, id)

Get Market Segmentation Group data.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.group_response_schema import GroupResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Group ID.

    try:
        # Get Market Segmentation Group data.
        api_response = api_instance.group_controller_single(x_property_id, id)
        print("The response of MarketSegmentationGroupsApi->group_controller_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Group ID. | 

### Return type

[**GroupResponseSchema**](GroupResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Market Segmentation Group data. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not Found response. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_controller_update**
> GroupResponseSchema group_controller_update(x_property_id, id, group_update_request_schema)

Update a Market Segmentation Group.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.group_response_schema import GroupResponseSchema
from cloudbeds_pms.models.group_update_request_schema import GroupUpdateRequestSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationGroupsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Group ID.
    group_update_request_schema = cloudbeds_pms.GroupUpdateRequestSchema() # GroupUpdateRequestSchema | Group data.

    try:
        # Update a Market Segmentation Group.
        api_response = api_instance.group_controller_update(x_property_id, id, group_update_request_schema)
        print("The response of MarketSegmentationGroupsApi->group_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationGroupsApi->group_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Group ID. | 
 **group_update_request_schema** | [**GroupUpdateRequestSchema**](GroupUpdateRequestSchema.md)| Group data. | 

### Return type

[**GroupResponseSchema**](GroupResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Market Segmentation Group. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

