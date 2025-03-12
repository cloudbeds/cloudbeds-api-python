# cloudbeds_pms.ImportTasksApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_task_controller_create**](ImportTasksApi.md#import_task_controller_create) | **POST** /import/v1/tasks | Create a new import task and generate a temporary upload URL.
[**import_task_controller_find_by_id**](ImportTasksApi.md#import_task_controller_find_by_id) | **GET** /import/v1/tasks/{taskId} | Fetch import task by ID.
[**import_task_controller_find_task_records**](ImportTasksApi.md#import_task_controller_find_task_records) | **GET** /import/v1/tasks/{taskId}/records | Fetch import task records by ID.
[**import_task_controller_get_all**](ImportTasksApi.md#import_task_controller_get_all) | **GET** /import/v1/tasks | Fetch a list of previously uploaded imports.


# **import_task_controller_create**
> ImportTaskResponseSchema import_task_controller_create(x_property_id, import_task_create_request_schema)

Create a new import task and generate a temporary upload URL.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.import_task_create_request_schema import ImportTaskCreateRequestSchema
from cloudbeds_pms.models.import_task_response_schema import ImportTaskResponseSchema
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
    api_instance = cloudbeds_pms.ImportTasksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    import_task_create_request_schema = cloudbeds_pms.ImportTaskCreateRequestSchema() # ImportTaskCreateRequestSchema | Import task create request

    try:
        # Create a new import task and generate a temporary upload URL.
        api_response = api_instance.import_task_controller_create(x_property_id, import_task_create_request_schema)
        print("The response of ImportTasksApi->import_task_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportTasksApi->import_task_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **import_task_create_request_schema** | [**ImportTaskCreateRequestSchema**](ImportTaskCreateRequestSchema.md)| Import task create request | 

### Return type

[**ImportTaskResponseSchema**](ImportTaskResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A new import task was created. |  -  |
**400** | Bad Request response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_task_controller_find_by_id**
> ImportTaskGetResponseSchema import_task_controller_find_by_id(x_property_id, task_id)

Fetch import task by ID.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.import_task_get_response_schema import ImportTaskGetResponseSchema
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
    api_instance = cloudbeds_pms.ImportTasksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    task_id = 1 # int | The import task ID

    try:
        # Fetch import task by ID.
        api_response = api_instance.import_task_controller_find_by_id(x_property_id, task_id)
        print("The response of ImportTasksApi->import_task_controller_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportTasksApi->import_task_controller_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **task_id** | **int**| The import task ID | 

### Return type

[**ImportTaskGetResponseSchema**](ImportTaskGetResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import task by ID. |  -  |
**404** | Not Found response |  -  |
**400** | Bad Request response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_task_controller_find_task_records**
> ImportTaskRecordListResponseSchema import_task_controller_find_task_records(x_property_id, task_id, limit=limit, offset=offset)

Fetch import task records by ID.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.import_task_record_list_response_schema import ImportTaskRecordListResponseSchema
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
    api_instance = cloudbeds_pms.ImportTasksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    task_id = 1 # int | The import task ID
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)

    try:
        # Fetch import task records by ID.
        api_response = api_instance.import_task_controller_find_task_records(x_property_id, task_id, limit=limit, offset=offset)
        print("The response of ImportTasksApi->import_task_controller_find_task_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportTasksApi->import_task_controller_find_task_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **task_id** | **int**| The import task ID | 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 

### Return type

[**ImportTaskRecordListResponseSchema**](ImportTaskRecordListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import task records by import task ID |  -  |
**404** | Not Found response |  -  |
**400** | Bad Request response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_task_controller_get_all**
> ImportTaskResponseSchema import_task_controller_get_all(x_property_id, limit=limit, offset=offset)

Fetch a list of previously uploaded imports.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.import_task_response_schema import ImportTaskResponseSchema
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
    api_instance = cloudbeds_pms.ImportTasksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    limit = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The maximum number of items to return in the response. Default is 100. (optional)
    offset = cloudbeds_pms.LimitOffsetPaginationSchema() # LimitOffsetPaginationSchema | The number of items to skip before starting to collect the result set. Used for pagination. (optional)

    try:
        # Fetch a list of previously uploaded imports.
        api_response = api_instance.import_task_controller_get_all(x_property_id, limit=limit, offset=offset)
        print("The response of ImportTasksApi->import_task_controller_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportTasksApi->import_task_controller_get_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **limit** | [**LimitOffsetPaginationSchema**](.md)| The maximum number of items to return in the response. Default is 100. | [optional] 
 **offset** | [**LimitOffsetPaginationSchema**](.md)| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] 

### Return type

[**ImportTaskResponseSchema**](ImportTaskResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of previously uploaded files/imports. |  -  |
**400** | Bad Request response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

