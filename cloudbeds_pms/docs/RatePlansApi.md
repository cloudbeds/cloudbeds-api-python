# cloudbeds_pms.RatePlansApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rate_plan_controller_create**](RatePlansApi.md#rate_plan_controller_create) | **POST** /rates/v1/rate-plans | Create a new Rate Plan.
[**rate_plan_controller_delete**](RatePlansApi.md#rate_plan_controller_delete) | **DELETE** /rates/v1/rate-plans/{id} | Delete a Rate Plan.
[**rate_plan_controller_index**](RatePlansApi.md#rate_plan_controller_index) | **GET** /rates/v1/rate-plans | Get a list of Rates Plans.
[**rate_plan_controller_single**](RatePlansApi.md#rate_plan_controller_single) | **GET** /rates/v1/rate-plans/{id} | Get Rate Plan data.
[**rate_plan_controller_update**](RatePlansApi.md#rate_plan_controller_update) | **PATCH** /rates/v1/rate-plans/{id} | Update an existing Rate Plan.


# **rate_plan_controller_create**
> RatePlanResponseSchema rate_plan_controller_create(x_property_id, rate_plan_create_request_schema)

Create a new Rate Plan.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.rate_plan_create_request_schema import RatePlanCreateRequestSchema
from cloudbeds_pms.models.rate_plan_response_schema import RatePlanResponseSchema
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
    api_instance = cloudbeds_pms.RatePlansApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    rate_plan_create_request_schema = cloudbeds_pms.RatePlanCreateRequestSchema() # RatePlanCreateRequestSchema | Rate Plan data.

    try:
        # Create a new Rate Plan.
        api_response = api_instance.rate_plan_controller_create(x_property_id, rate_plan_create_request_schema)
        print("The response of RatePlansApi->rate_plan_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlansApi->rate_plan_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **rate_plan_create_request_schema** | [**RatePlanCreateRequestSchema**](RatePlanCreateRequestSchema.md)| Rate Plan data. | 

### Return type

[**RatePlanResponseSchema**](RatePlanResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Rate Plan. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_plan_controller_delete**
> object rate_plan_controller_delete(x_property_id, id)

Delete a Rate Plan.

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
    api_instance = cloudbeds_pms.RatePlansApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Rate Plan ID.

    try:
        # Delete a Rate Plan.
        api_response = api_instance.rate_plan_controller_delete(x_property_id, id)
        print("The response of RatePlansApi->rate_plan_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlansApi->rate_plan_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Rate Plan ID. | 

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
**204** | Rate Plan was deleted. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_plan_controller_index**
> RatePlanListResponseSchema rate_plan_controller_index(x_property_id, offset=offset, limit=limit, filters=filters, sort=sort, include_total=include_total)

Get a list of Rates Plans.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.rate_plan_list_response_schema import RatePlanListResponseSchema
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
    api_instance = cloudbeds_pms.RatePlansApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    filters = 'isActive:equals:true;status:in:active,expired;policyId:in:1,2;derivedRatePlanId:is_null' # str | Filter the list. Each clause is written field:operator:value, and multiple clauses are separated by a semicolon (;) — not a comma, which the sort parameter uses. Clauses are combined with AND; grouping and OR are not supported here. Supported fields: isActive (equals), isDerived (equals), promoCode (contains), status (equals, in), policyId (equals, in), segmentId (equals, in), derivedRatePlanId (equals, in, is_null, is_not_null). A status filter takes one of active, expired, no-intervals, disabled; with `in`, several separated by a comma. It is applied before limit and offset, so a page and its total both describe the rate plans in those statuses. The in operator takes a comma-separated list of up to 100 IDs (policyId:in:1,2,3); is_null and is_not_null take no value (derivedRatePlanId:is_null). derivedRatePlanId takes 0 for the property base rate, alone or in a list (derivedRatePlanId:in:0,12), and 0 matches plans with no parent plan. derivedRatePlanId:is_null matches plans with no parent plan, which includes plans derived from the base rate; derivedRatePlanId:is_not_null matches plans whose parent is another rate plan. None of these checks isDerived, so add isDerived:equals:true to keep derived plans only. policyId, segmentId and derivedRatePlanId are filters only and cannot be sorted on. (optional)
    sort = 'createdAt:desc,updatedAt:asc' # str | Sort the list. Supported fields: createdAt, updatedAt, isActive, status. Multiple fields are separated by a comma (,), and each may carry a direction written as field:asc or field:desc; a field given on its own sorts ascending. status sorts in the order active, expired, no-intervals, disabled (reversed for desc). When omitted, the list is returned newest first (createdAt descending). (optional)
    include_total = False # bool | Return the total number of items matching the request, ignoring limit and offset. Boolean values are accepted case-insensitively, so true, TRUE, True and 1 all enable it. (optional) (default to False)

    try:
        # Get a list of Rates Plans.
        api_response = api_instance.rate_plan_controller_index(x_property_id, offset=offset, limit=limit, filters=filters, sort=sort, include_total=include_total)
        print("The response of RatePlansApi->rate_plan_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlansApi->rate_plan_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **filters** | **str**| Filter the list. Each clause is written field:operator:value, and multiple clauses are separated by a semicolon (;) — not a comma, which the sort parameter uses. Clauses are combined with AND; grouping and OR are not supported here. Supported fields: isActive (equals), isDerived (equals), promoCode (contains), status (equals, in), policyId (equals, in), segmentId (equals, in), derivedRatePlanId (equals, in, is_null, is_not_null). A status filter takes one of active, expired, no-intervals, disabled; with &#x60;in&#x60;, several separated by a comma. It is applied before limit and offset, so a page and its total both describe the rate plans in those statuses. The in operator takes a comma-separated list of up to 100 IDs (policyId:in:1,2,3); is_null and is_not_null take no value (derivedRatePlanId:is_null). derivedRatePlanId takes 0 for the property base rate, alone or in a list (derivedRatePlanId:in:0,12), and 0 matches plans with no parent plan. derivedRatePlanId:is_null matches plans with no parent plan, which includes plans derived from the base rate; derivedRatePlanId:is_not_null matches plans whose parent is another rate plan. None of these checks isDerived, so add isDerived:equals:true to keep derived plans only. policyId, segmentId and derivedRatePlanId are filters only and cannot be sorted on. | [optional] 
 **sort** | **str**| Sort the list. Supported fields: createdAt, updatedAt, isActive, status. Multiple fields are separated by a comma (,), and each may carry a direction written as field:asc or field:desc; a field given on its own sorts ascending. status sorts in the order active, expired, no-intervals, disabled (reversed for desc). When omitted, the list is returned newest first (createdAt descending). | [optional] 
 **include_total** | **bool**| Return the total number of items matching the request, ignoring limit and offset. Boolean values are accepted case-insensitively, so true, TRUE, True and 1 all enable it. | [optional] [default to False]

### Return type

[**RatePlanListResponseSchema**](RatePlanListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Rates Plans. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_plan_controller_single**
> RatePlanResponseSchema rate_plan_controller_single(x_property_id, id)

Get Rate Plan data.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.rate_plan_response_schema import RatePlanResponseSchema
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
    api_instance = cloudbeds_pms.RatePlansApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Rate Plan ID.

    try:
        # Get Rate Plan data.
        api_response = api_instance.rate_plan_controller_single(x_property_id, id)
        print("The response of RatePlansApi->rate_plan_controller_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlansApi->rate_plan_controller_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Rate Plan ID. | 

### Return type

[**RatePlanResponseSchema**](RatePlanResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate Plan data. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not Found response. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_plan_controller_update**
> RatePlanResponseSchema rate_plan_controller_update(x_property_id, id, rate_plan_update_request_schema)

Update an existing Rate Plan.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.rate_plan_response_schema import RatePlanResponseSchema
from cloudbeds_pms.models.rate_plan_update_request_schema import RatePlanUpdateRequestSchema
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
    api_instance = cloudbeds_pms.RatePlansApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    id = cloudbeds_pms.Id() # Id | Rate Plan ID.
    rate_plan_update_request_schema = cloudbeds_pms.RatePlanUpdateRequestSchema() # RatePlanUpdateRequestSchema | Rate Plan data.

    try:
        # Update an existing Rate Plan.
        api_response = api_instance.rate_plan_controller_update(x_property_id, id, rate_plan_update_request_schema)
        print("The response of RatePlansApi->rate_plan_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatePlansApi->rate_plan_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **id** | **Id**| Rate Plan ID. | 
 **rate_plan_update_request_schema** | [**RatePlanUpdateRequestSchema**](RatePlanUpdateRequestSchema.md)| Rate Plan data. | 

### Return type

[**RatePlanResponseSchema**](RatePlanResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Rate Plan. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**404** | Not found response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

