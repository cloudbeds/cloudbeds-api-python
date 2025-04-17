# cloudbeds_pms_v1_2.HouseAccountApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_house_account_list_get**](HouseAccountApi.md#get_house_account_list_get) | **GET** /getHouseAccountList | getHouseAccountList
[**post_new_house_account_post**](HouseAccountApi.md#post_new_house_account_post) | **POST** /postNewHouseAccount | postNewHouseAccount
[**put_house_account_status_put**](HouseAccountApi.md#put_house_account_status_put) | **PUT** /putHouseAccountStatus | putHouseAccountStatus


# **get_house_account_list_get**
> GetHouseAccountListResponse get_house_account_list_get(property_id=property_id)

getHouseAccountList

Pulls list of active house accounts

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_house_account_list_response import GetHouseAccountListResponse
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
    api_instance = cloudbeds_pms_v1_2.HouseAccountApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getHouseAccountList
        api_response = api_instance.get_house_account_list_get(property_id=property_id)
        print("The response of HouseAccountApi->get_house_account_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HouseAccountApi->get_house_account_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetHouseAccountListResponse**](GetHouseAccountListResponse.md)

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

# **post_new_house_account_post**
> PostNewHouseAccountResponse post_new_house_account_post(property_id=property_id, account_name=account_name, is_private=is_private)

postNewHouseAccount

Add a new House Account

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_new_house_account_response import PostNewHouseAccountResponse
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
    api_instance = cloudbeds_pms_v1_2.HouseAccountApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    account_name = 'account_name_example' # str | House Account name (optional)
    is_private = False # bool | Whether House Account is available only to user (optional) (default to False)

    try:
        # postNewHouseAccount
        api_response = api_instance.post_new_house_account_post(property_id=property_id, account_name=account_name, is_private=is_private)
        print("The response of HouseAccountApi->post_new_house_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HouseAccountApi->post_new_house_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **account_name** | **str**| House Account name | [optional] 
 **is_private** | **bool**| Whether House Account is available only to user | [optional] [default to False]

### Return type

[**PostNewHouseAccountResponse**](PostNewHouseAccountResponse.md)

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

# **put_house_account_status_put**
> PutHouseAccountStatusResponse put_house_account_status_put(property_id=property_id, house_account_id=house_account_id, status=status)

putHouseAccountStatus

Change specific house account to either open or closed.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.put_house_account_status_response import PutHouseAccountStatusResponse
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
    api_instance = cloudbeds_pms_v1_2.HouseAccountApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    house_account_id = 'house_account_id_example' # str | House Account ID (optional)
    status = 'status_example' # str | House Account status (optional)

    try:
        # putHouseAccountStatus
        api_response = api_instance.put_house_account_status_put(property_id=property_id, house_account_id=house_account_id, status=status)
        print("The response of HouseAccountApi->put_house_account_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HouseAccountApi->put_house_account_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **house_account_id** | **str**| House Account ID | [optional] 
 **status** | **str**| House Account status | [optional] 

### Return type

[**PutHouseAccountStatusResponse**](PutHouseAccountStatusResponse.md)

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

