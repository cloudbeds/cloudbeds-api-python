# cloudbeds_pms.MarketSegmentationSegmentsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segment_controller_create**](MarketSegmentationSegmentsApi.md#segment_controller_create) | **POST** /market-segmentation/v1/segments | Create a new Market Segmentation Segment.
[**segment_controller_default**](MarketSegmentationSegmentsApi.md#segment_controller_default) | **POST** /market-segmentation/v1/segments/{id}/default | Set Market Segmentation Segment as Default.
[**segment_controller_delete**](MarketSegmentationSegmentsApi.md#segment_controller_delete) | **DELETE** /market-segmentation/v1/segments/{id} | Delete a Market Segmentation Segment.
[**segment_controller_disable**](MarketSegmentationSegmentsApi.md#segment_controller_disable) | **POST** /market-segmentation/v1/segments/{id}/disable | Disable a Market Segmentation Segment.
[**segment_controller_enable**](MarketSegmentationSegmentsApi.md#segment_controller_enable) | **POST** /market-segmentation/v1/segments/{id}/enable | Enable a Market Segmentation Segment.
[**segment_controller_index**](MarketSegmentationSegmentsApi.md#segment_controller_index) | **GET** /market-segmentation/v1/segments/{enabled} | Get a list of Market Segmentation Segments.
[**segment_controller_reservations**](MarketSegmentationSegmentsApi.md#segment_controller_reservations) | **GET** /market-segmentation/v1/segments/{id}/reservations/{active} | Get a list of reservations linked to a Market Segmentation Segment.
[**segment_controller_single**](MarketSegmentationSegmentsApi.md#segment_controller_single) | **GET** /market-segmentation/v1/segments/{id} | Get Market Segmentation Segment data.
[**segment_controller_update**](MarketSegmentationSegmentsApi.md#segment_controller_update) | **PATCH** /market-segmentation/v1/segments/{id} | Update a Market Segmentation Segment.


# **segment_controller_create**
> SegmentResponseSchema segment_controller_create(x_property_id, segment_create_request_schema)

Create a new Market Segmentation Segment.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.segment_create_request_schema import SegmentCreateRequestSchema
from cloudbeds_pms.models.segment_response_schema import SegmentResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    segment_create_request_schema = cloudbeds_pms.SegmentCreateRequestSchema() # SegmentCreateRequestSchema | Segment data.

    try:
        # Create a new Market Segmentation Segment.
        api_response = api_instance.segment_controller_create(x_property_id, segment_create_request_schema)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **segment_create_request_schema** | [**SegmentCreateRequestSchema**](SegmentCreateRequestSchema.md)| Segment data. | 

### Return type

[**SegmentResponseSchema**](SegmentResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Market Segmentation Segment. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_default**
> object segment_controller_default(x_property_id, id)

Set Market Segmentation Segment as Default.

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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.

    try:
        # Set Market Segmentation Segment as Default.
        api_response = api_instance.segment_controller_default(x_property_id, id)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 

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
**204** | Market Segmentation Segment was set as default. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_delete**
> object segment_controller_delete(x_property_id, id)

Delete a Market Segmentation Segment.

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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.

    try:
        # Delete a Market Segmentation Segment.
        api_response = api_instance.segment_controller_delete(x_property_id, id)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 

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
**204** | Market Segmentation Segment was deleted. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_disable**
> object segment_controller_disable(x_property_id, id)

Disable a Market Segmentation Segment.

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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.

    try:
        # Disable a Market Segmentation Segment.
        api_response = api_instance.segment_controller_disable(x_property_id, id)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 

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
**204** | Market Segmentation Segment was disabled. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_enable**
> object segment_controller_enable(x_property_id, id)

Enable a Market Segmentation Segment.

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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.

    try:
        # Enable a Market Segmentation Segment.
        api_response = api_instance.segment_controller_enable(x_property_id, id)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 

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
**204** | Market Segmentation Segment was enabled. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_index**
> SegmentListResponseSchema segment_controller_index(x_property_id, enabled, offset=offset, limit=limit, filters=filters)

Get a list of Market Segmentation Segments.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.enabled import Enabled
from cloudbeds_pms.models.limit_offset_pagination_schema import LimitOffsetPaginationSchema
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema
from cloudbeds_pms.models.segment_list_response_schema import SegmentListResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    enabled = cloudbeds_pms.Enabled() # Enabled | List only enabled segments.
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)
    filters = cloudbeds_pms.QueryParameterDynamicFilterSchema() # QueryParameterDynamicFilterSchema | This parameter should be formatted as a list of strings separated by ; (optional)

    try:
        # Get a list of Market Segmentation Segments.
        api_response = api_instance.segment_controller_index(x_property_id, enabled, offset=offset, limit=limit, filters=filters)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **enabled** | [**Enabled**](.md)| List only enabled segments. | 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 
 **filters** | [**QueryParameterDynamicFilterSchema**](.md)| This parameter should be formatted as a list of strings separated by ; | [optional] 

### Return type

[**SegmentListResponseSchema**](SegmentListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Market Segmentation Segments. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_reservations**
> SegmentListReservationsResponseSchema segment_controller_reservations(x_property_id, id, active, offset=offset, limit=limit)

Get a list of reservations linked to a Market Segmentation Segment.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.active import Active
from cloudbeds_pms.models.id import Id
from cloudbeds_pms.models.limit_offset_pagination_schema import LimitOffsetPaginationSchema
from cloudbeds_pms.models.segment_list_reservations_response_schema import SegmentListReservationsResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.
    active = cloudbeds_pms.Active() # Active | List only active reservations.
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)

    try:
        # Get a list of reservations linked to a Market Segmentation Segment.
        api_response = api_instance.segment_controller_reservations(x_property_id, id, active, offset=offset, limit=limit)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | [**Id**](.md)| Segment ID. | 
 **active** | [**Active**](.md)| List only active reservations. | 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 

### Return type

[**SegmentListReservationsResponseSchema**](SegmentListReservationsResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of reservations linked to a Market Segmentation Segment. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_single**
> SegmentResponseSchema segment_controller_single(x_property_id, id)

Get Market Segmentation Segment data.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.segment_response_schema import SegmentResponseSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.

    try:
        # Get Market Segmentation Segment data.
        api_response = api_instance.segment_controller_single(x_property_id, id)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 

### Return type

[**SegmentResponseSchema**](SegmentResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Market Segmentation Segment data. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not Found response. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_controller_update**
> SegmentResponseSchema segment_controller_update(x_property_id, id, segment_update_request_schema)

Update a Market Segmentation Segment.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.segment_response_schema import SegmentResponseSchema
from cloudbeds_pms.models.segment_update_request_schema import SegmentUpdateRequestSchema
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
    api_instance = cloudbeds_pms.MarketSegmentationSegmentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Segment ID.
    segment_update_request_schema = cloudbeds_pms.SegmentUpdateRequestSchema() # SegmentUpdateRequestSchema | Segment data.

    try:
        # Update a Market Segmentation Segment.
        api_response = api_instance.segment_controller_update(x_property_id, id, segment_update_request_schema)
        print("The response of MarketSegmentationSegmentsApi->segment_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketSegmentationSegmentsApi->segment_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Segment ID. | 
 **segment_update_request_schema** | [**SegmentUpdateRequestSchema**](SegmentUpdateRequestSchema.md)| Segment data. | 

### Return type

[**SegmentResponseSchema**](SegmentResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Market Segmentation Segment. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

