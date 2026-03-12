# cloudbeds_pms.SmartPolicyExceptionsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_exception_controller_create**](SmartPolicyExceptionsApi.md#policy_exception_controller_create) | **POST** /smart-policies/v1/exceptions | Create a new policy exception.
[**policy_exception_controller_destroy**](SmartPolicyExceptionsApi.md#policy_exception_controller_destroy) | **DELETE** /smart-policies/v1/exceptions/{exceptionId} | Delete a policy exception.
[**policy_exception_controller_eligible_rates**](SmartPolicyExceptionsApi.md#policy_exception_controller_eligible_rates) | **GET** /smart-policies/v1/exceptions/eligible-rates | Get eligible rate plans and base rates for exception creation.
[**policy_exception_controller_index**](SmartPolicyExceptionsApi.md#policy_exception_controller_index) | **GET** /smart-policies/v1/exceptions | List all policy exceptions for a property.
[**policy_exception_controller_partial_update**](SmartPolicyExceptionsApi.md#policy_exception_controller_partial_update) | **PATCH** /smart-policies/v1/exceptions/{exceptionId} | Partially update a policy exception.
[**policy_exception_controller_show**](SmartPolicyExceptionsApi.md#policy_exception_controller_show) | **GET** /smart-policies/v1/exceptions/{exceptionId} | Get a single policy exception by ID.
[**policy_exception_controller_update**](SmartPolicyExceptionsApi.md#policy_exception_controller_update) | **PUT** /smart-policies/v1/exceptions/{exceptionId} | Update an existing policy exception.


# **policy_exception_controller_create**
> PolicyExceptionResponseSchema policy_exception_controller_create(x_property_id, create_policy_exception_request_schema)

Create a new policy exception.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.create_policy_exception_request_schema import CreatePolicyExceptionRequestSchema
from cloudbeds_pms.models.policy_exception_response_schema import PolicyExceptionResponseSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    create_policy_exception_request_schema = cloudbeds_pms.CreatePolicyExceptionRequestSchema() # CreatePolicyExceptionRequestSchema | Policy exception data.

    try:
        # Create a new policy exception.
        api_response = api_instance.policy_exception_controller_create(x_property_id, create_policy_exception_request_schema)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **create_policy_exception_request_schema** | [**CreatePolicyExceptionRequestSchema**](CreatePolicyExceptionRequestSchema.md)| Policy exception data. | 

### Return type

[**PolicyExceptionResponseSchema**](PolicyExceptionResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created policy exception. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**409** | Conflict response (exception overlaps with existing exception). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_destroy**
> object policy_exception_controller_destroy(x_property_id, exception_id)

Delete a policy exception.

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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    exception_id = cloudbeds_pms.ExceptionId() # ExceptionId | Policy exception ID.

    try:
        # Delete a policy exception.
        api_response = api_instance.policy_exception_controller_destroy(x_property_id, exception_id)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **exception_id** | **ExceptionId**| Policy exception ID. | 

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
**204** | Policy exception was deleted. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_eligible_rates**
> EligibleRatesResponseSchema policy_exception_controller_eligible_rates(x_property_id, start_date, end_date, limit=limit, offset=offset, sort=sort)

Get eligible rate plans and base rates for exception creation.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.eligible_rates_response_schema import EligibleRatesResponseSchema
from cloudbeds_pms.models.query_parameter_sort_schema import QueryParameterSortSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    start_date = 'Mon Jan 01 00:00:00 UTC 2024' # date | Start date of the date range to filter rate plans (YYYY-MM-DD).
    end_date = 'Wed Jan 31 00:00:00 UTC 2024' # date | End date of the date range to filter rate plans (YYYY-MM-DD).
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    sort = cloudbeds_pms.QueryParameterSortSchema() # QueryParameterSortSchema | A string specifying fields for sorting with optional directions (e.g., asc or desc). (optional)

    try:
        # Get eligible rate plans and base rates for exception creation.
        api_response = api_instance.policy_exception_controller_eligible_rates(x_property_id, start_date, end_date, limit=limit, offset=offset, sort=sort)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_eligible_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_eligible_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **start_date** | **date**| Start date of the date range to filter rate plans (YYYY-MM-DD). | 
 **end_date** | **date**| End date of the date range to filter rate plans (YYYY-MM-DD). | 
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **sort** | [**QueryParameterSortSchema**](.md)| A string specifying fields for sorting with optional directions (e.g., asc or desc). | [optional] 

### Return type

[**EligibleRatesResponseSchema**](EligibleRatesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Eligible rate plans and base rates. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_index**
> PolicyExceptionListResponseSchema policy_exception_controller_index(x_property_id, policy_root_id=policy_root_id, limit=limit, offset=offset, sort=sort)

List all policy exceptions for a property.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.policy_exception_list_response_schema import PolicyExceptionListResponseSchema
from cloudbeds_pms.models.query_parameter_sort_schema import QueryParameterSortSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    policy_root_id = '5001' # str | Filter by smart policy root ID. (optional)
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    sort = cloudbeds_pms.QueryParameterSortSchema() # QueryParameterSortSchema | A string specifying fields for sorting with optional directions (e.g., asc or desc). (optional)

    try:
        # List all policy exceptions for a property.
        api_response = api_instance.policy_exception_controller_index(x_property_id, policy_root_id=policy_root_id, limit=limit, offset=offset, sort=sort)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **policy_root_id** | **str**| Filter by smart policy root ID. | [optional] 
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **sort** | [**QueryParameterSortSchema**](.md)| A string specifying fields for sorting with optional directions (e.g., asc or desc). | [optional] 

### Return type

[**PolicyExceptionListResponseSchema**](PolicyExceptionListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of policy exceptions. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_partial_update**
> PolicyExceptionResponseSchema policy_exception_controller_partial_update(x_property_id, exception_id, patch_policy_exception_request_schema)

Partially update a policy exception.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.patch_policy_exception_request_schema import PatchPolicyExceptionRequestSchema
from cloudbeds_pms.models.policy_exception_response_schema import PolicyExceptionResponseSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    exception_id = cloudbeds_pms.ExceptionId() # ExceptionId | Policy exception ID.
    patch_policy_exception_request_schema = cloudbeds_pms.PatchPolicyExceptionRequestSchema() # PatchPolicyExceptionRequestSchema | Policy exception fields to update.

    try:
        # Partially update a policy exception.
        api_response = api_instance.policy_exception_controller_partial_update(x_property_id, exception_id, patch_policy_exception_request_schema)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **exception_id** | **ExceptionId**| Policy exception ID. | 
 **patch_policy_exception_request_schema** | [**PatchPolicyExceptionRequestSchema**](PatchPolicyExceptionRequestSchema.md)| Policy exception fields to update. | 

### Return type

[**PolicyExceptionResponseSchema**](PolicyExceptionResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated policy exception. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**409** | Conflict response (exception overlaps with existing exception). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_show**
> PolicyExceptionResponseSchema policy_exception_controller_show(x_property_id, exception_id)

Get a single policy exception by ID.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.policy_exception_response_schema import PolicyExceptionResponseSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    exception_id = cloudbeds_pms.ExceptionId() # ExceptionId | Policy exception ID.

    try:
        # Get a single policy exception by ID.
        api_response = api_instance.policy_exception_controller_show(x_property_id, exception_id)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **exception_id** | **ExceptionId**| Policy exception ID. | 

### Return type

[**PolicyExceptionResponseSchema**](PolicyExceptionResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy exception details. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_exception_controller_update**
> PolicyExceptionResponseSchema policy_exception_controller_update(x_property_id, exception_id, update_policy_exception_request_schema)

Update an existing policy exception.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.policy_exception_response_schema import PolicyExceptionResponseSchema
from cloudbeds_pms.models.update_policy_exception_request_schema import UpdatePolicyExceptionRequestSchema
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
    api_instance = cloudbeds_pms.SmartPolicyExceptionsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    exception_id = cloudbeds_pms.ExceptionId() # ExceptionId | Policy exception ID.
    update_policy_exception_request_schema = cloudbeds_pms.UpdatePolicyExceptionRequestSchema() # UpdatePolicyExceptionRequestSchema | Policy exception data.

    try:
        # Update an existing policy exception.
        api_response = api_instance.policy_exception_controller_update(x_property_id, exception_id, update_policy_exception_request_schema)
        print("The response of SmartPolicyExceptionsApi->policy_exception_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPolicyExceptionsApi->policy_exception_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **exception_id** | **ExceptionId**| Policy exception ID. | 
 **update_policy_exception_request_schema** | [**UpdatePolicyExceptionRequestSchema**](UpdatePolicyExceptionRequestSchema.md)| Policy exception data. | 

### Return type

[**PolicyExceptionResponseSchema**](PolicyExceptionResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated policy exception. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**409** | Conflict response (exception overlaps with existing exception). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

