# cloudbeds_pms_v1_3.CRMApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_cache_remove_post**](CRMApi.md#crm_cache_remove_post) | **POST** /crm/cache_remove | PostCRMCacheRemove
[**crm_cache_update_post**](CRMApi.md#crm_cache_update_post) | **POST** /crm/cache_update | PostCRMCacheUpdate


# **crm_cache_remove_post**
> PostCRMCacheRemoveResponse crm_cache_remove_post(property_id=property_id, association_id=association_id)

PostCRMCacheRemove



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_crm_cache_remove_response import PostCRMCacheRemoveResponse
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
    api_instance = cloudbeds_pms_v1_3.CRMApi(api_client)
    property_id = ['property_id_example'] # List[str] | Property IDs that needs the cache to be removed (optional)
    association_id = 'association_id_example' # str | Association ID that needs the cache to be removed (optional)

    try:
        # PostCRMCacheRemove
        api_response = api_instance.crm_cache_remove_post(property_id=property_id, association_id=association_id)
        print("The response of CRMApi->crm_cache_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRMApi->crm_cache_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | [**List[str]**](str.md)| Property IDs that needs the cache to be removed | [optional] 
 **association_id** | **str**| Association ID that needs the cache to be removed | [optional] 

### Return type

[**PostCRMCacheRemoveResponse**](PostCRMCacheRemoveResponse.md)

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

# **crm_cache_update_post**
> PostCRMCacheUpdateResponse crm_cache_update_post(property_id=property_id, clear=clear, clear_packages=clear_packages)

PostCRMCacheUpdate



### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_crm_cache_update_response import PostCRMCacheUpdateResponse
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
    api_instance = cloudbeds_pms_v1_3.CRMApi(api_client)
    property_id = 'property_id_example' # str | Property ID that needs the cache to be updated (optional)
    clear = True # bool | If property cache should be cleared (optional)
    clear_packages = True # bool | If packages cache should be cleared for the property (optional)

    try:
        # PostCRMCacheUpdate
        api_response = api_instance.crm_cache_update_post(property_id=property_id, clear=clear, clear_packages=clear_packages)
        print("The response of CRMApi->crm_cache_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CRMApi->crm_cache_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID that needs the cache to be updated | [optional] 
 **clear** | **bool**| If property cache should be cleared | [optional] 
 **clear_packages** | **bool**| If packages cache should be cleared for the property | [optional] 

### Return type

[**PostCRMCacheUpdateResponse**](PostCRMCacheUpdateResponse.md)

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

