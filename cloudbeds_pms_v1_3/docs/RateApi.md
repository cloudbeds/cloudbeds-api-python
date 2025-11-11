# cloudbeds_pms_v1_3.RateApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_get**](RateApi.md#get_rate_get) | **GET** /getRate | getRate
[**get_rate_jobs_get**](RateApi.md#get_rate_jobs_get) | **GET** /getRateJobs | getRateJobs
[**get_rate_plans_get**](RateApi.md#get_rate_plans_get) | **GET** /getRatePlans | getRatePlans
[**patch_rate_post**](RateApi.md#patch_rate_post) | **POST** /patchRate | patchRate
[**put_rate_post**](RateApi.md#put_rate_post) | **POST** /putRate | putRate


# **get_rate_get**
> GetRateResponse get_rate_get(room_type_id, start_date, end_date, adults=adults, children=children, detailed_rates=detailed_rates, promo_code=promo_code)

getRate

Returns the rate of the room type selected, based on the provided parameters

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rate_response import GetRateResponse
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
    api_instance = cloudbeds_pms_v1_3.RateApi(api_client)
    room_type_id = 'room_type_id_example' # str | Room Type ID
    start_date = '2013-10-20' # date | Check-in date
    end_date = '2013-10-20' # date | Check-out date
    adults = 56 # int | Number of adults (optional)
    children = 56 # int | Number of children (optional)
    detailed_rates = False # bool | If the rates need detailed information (optional) (default to False)
    promo_code = False # bool | Return information for one or more specific rate plans by promo code. This parameter is DEPRECATED and not recommended for usage. Use method getRatePlans instead (optional) (default to False)

    try:
        # getRate
        api_response = api_instance.get_rate_get(room_type_id, start_date, end_date, adults=adults, children=children, detailed_rates=detailed_rates, promo_code=promo_code)
        print("The response of RateApi->get_rate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->get_rate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_type_id** | **str**| Room Type ID | 
 **start_date** | **date**| Check-in date | 
 **end_date** | **date**| Check-out date | 
 **adults** | **int**| Number of adults | [optional] 
 **children** | **int**| Number of children | [optional] 
 **detailed_rates** | **bool**| If the rates need detailed information | [optional] [default to False]
 **promo_code** | **bool**| Return information for one or more specific rate plans by promo code. This parameter is DEPRECATED and not recommended for usage. Use method getRatePlans instead | [optional] [default to False]

### Return type

[**GetRateResponse**](GetRateResponse.md)

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

# **get_rate_jobs_get**
> GetRateJobsResponse get_rate_jobs_get(job_reference_id=job_reference_id, status=status)

getRateJobs

Returns a list of Rate Jobs. Rate jobs are only returned within 7 days of creation, after 7 days they will not be returned in the response. Requests which do not provide a jobReferenceID will be filtered by the client ID of the request's token.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rate_jobs_response import GetRateJobsResponse
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
    api_instance = cloudbeds_pms_v1_3.RateApi(api_client)
    job_reference_id = 'job_reference_id_example' # str | Filter Rate Jobs by jobReferenceID (optional)
    status = 'status_example' # str | Filter Rate Jobs based on status (optional)

    try:
        # getRateJobs
        api_response = api_instance.get_rate_jobs_get(job_reference_id=job_reference_id, status=status)
        print("The response of RateApi->get_rate_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->get_rate_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_reference_id** | **str**| Filter Rate Jobs by jobReferenceID | [optional] 
 **status** | **str**| Filter Rate Jobs based on status | [optional] 

### Return type

[**GetRateJobsResponse**](GetRateJobsResponse.md)

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

# **get_rate_plans_get**
> GetRatePlansResponse get_rate_plans_get(start_date, end_date, property_ids=property_ids, rate_ids=rate_ids, room_type_id=room_type_id, promo_code=promo_code, include_promo_code=include_promo_code, adults=adults, children=children, detailed_rates=detailed_rates, include_shared_rooms=include_shared_rooms)

getRatePlans

Returns the rates of the room type or promo code selected, based on the provided parameters. If no parameters are provided, then the method will return all publicly available rate plans. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_rate_plans_response import GetRatePlansResponse
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
    api_instance = cloudbeds_pms_v1_3.RateApi(api_client)
    start_date = '2013-10-20' # date | Check-in date
    end_date = '2013-10-20' # date | Check-out date
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)
    rate_ids = 'rate_ids_example' # str | List of Rate IDs, comma-separated, i.e. 37,345,89 (optional)
    room_type_id = 'room_type_id_example' # str | List of Room Type IDs, comma-separated, i.e. 37,345,89 (optional)
    promo_code = 'promo_code_example' # str | List of Promo Codes, comma-separated, i.e. 37,345,89 (optional)
    include_promo_code = True # bool | Include rate plans with promo code (optional) (default to True)
    adults = 56 # int | Number of adults (optional)
    children = 56 # int | Number of children (optional)
    detailed_rates = False # bool | If the rates need detailed information (optional) (default to False)
    include_shared_rooms = False # bool | Include shared rooms in the result for multiple adults/children (optional) (default to False)

    try:
        # getRatePlans
        api_response = api_instance.get_rate_plans_get(start_date, end_date, property_ids=property_ids, rate_ids=rate_ids, room_type_id=room_type_id, promo_code=promo_code, include_promo_code=include_promo_code, adults=adults, children=children, detailed_rates=detailed_rates, include_shared_rooms=include_shared_rooms)
        print("The response of RateApi->get_rate_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->get_rate_plans_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Check-in date | 
 **end_date** | **date**| Check-out date | 
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **rate_ids** | **str**| List of Rate IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **room_type_id** | **str**| List of Room Type IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **promo_code** | **str**| List of Promo Codes, comma-separated, i.e. 37,345,89 | [optional] 
 **include_promo_code** | **bool**| Include rate plans with promo code | [optional] [default to True]
 **adults** | **int**| Number of adults | [optional] 
 **children** | **int**| Number of children | [optional] 
 **detailed_rates** | **bool**| If the rates need detailed information | [optional] [default to False]
 **include_shared_rooms** | **bool**| Include shared rooms in the result for multiple adults/children | [optional] [default to False]

### Return type

[**GetRatePlansResponse**](GetRatePlansResponse.md)

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

# **patch_rate_post**
> PostPatchRateResponse patch_rate_post(rates=rates)

patchRate

Update the rate of the room based on rateID selected, based on the provided parameters. You can make multiple rate updates in a single API call. Providing a startDate and/or endDate will update rates only within the interval provided. Only non derived rates can be updated, requests to update a derived rate will return an error. This endpoint performs updates asynchronously,  rate updates are added to a queue and the endpoint returns a job reference ID. This job reference ID can be used to track job status notifications or to look up details of the update once it is completed. The API is limited to 30 interval per update, sending more than 30 will return an error.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_patch_rate_request_rates_inner import PostPatchRateRequestRatesInner
from cloudbeds_pms_v1_3.models.post_patch_rate_response import PostPatchRateResponse
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
    api_instance = cloudbeds_pms_v1_3.RateApi(api_client)
    rates = [cloudbeds_pms_v1_3.PostPatchRateRequestRatesInner()] # List[PostPatchRateRequestRatesInner] | Array of rates to update (optional)

    try:
        # patchRate
        api_response = api_instance.patch_rate_post(rates=rates)
        print("The response of RateApi->patch_rate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->patch_rate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rates** | [**List[PostPatchRateRequestRatesInner]**](PostPatchRateRequestRatesInner.md)| Array of rates to update | [optional] 

### Return type

[**PostPatchRateResponse**](PostPatchRateResponse.md)

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

# **put_rate_post**
> PostPutRateResponse put_rate_post(rates=rates)

putRate

Update the rate of the room based on rateID selected, based on the provided parameters. You can make multiple rate updates in a single API call. Providing a startDate and/or endDate will update rates only within the interval provided. Only non derived rates can be updated, requests to update a derived rate will return an error. This endpoint performs updates asynchronously,  rate updates are added to a queue and the endpoint returns a job reference ID. This job reference ID can be used to track job status notifications or to look up details of the update once it is completed. The API is limited to 30 interval per update, sending more than 30 will return an error.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_put_rate_request_rates_inner import PostPutRateRequestRatesInner
from cloudbeds_pms_v1_3.models.post_put_rate_response import PostPutRateResponse
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
    api_instance = cloudbeds_pms_v1_3.RateApi(api_client)
    rates = [cloudbeds_pms_v1_3.PostPutRateRequestRatesInner()] # List[PostPutRateRequestRatesInner] | Array of rates to update (optional)

    try:
        # putRate
        api_response = api_instance.put_rate_post(rates=rates)
        print("The response of RateApi->put_rate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->put_rate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rates** | [**List[PostPutRateRequestRatesInner]**](PostPutRateRequestRatesInner.md)| Array of rates to update | [optional] 

### Return type

[**PostPutRateResponse**](PostPutRateResponse.md)

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

