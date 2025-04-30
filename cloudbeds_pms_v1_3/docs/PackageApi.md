# cloudbeds_pms_v1_3.PackageApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package_names_get**](PackageApi.md#get_package_names_get) | **GET** /getPackageNames | getPackageNames
[**get_packages_get**](PackageApi.md#get_packages_get) | **GET** /getPackages | getPackages


# **get_package_names_get**
> GetPackagesResponse get_package_names_get(property_id=property_id)

getPackageNames

Return a list of billing package names for a property

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_packages_response import GetPackagesResponse
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
    api_instance = cloudbeds_pms_v1_3.PackageApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getPackageNames
        api_response = api_instance.get_package_names_get(property_id=property_id)
        print("The response of PackageApi->get_package_names_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->get_package_names_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetPackagesResponse**](GetPackagesResponse.md)

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

# **get_packages_get**
> GetPackagesResponse get_packages_get(property_id=property_id)

getPackages

This efficient method allows you to retrieve the collection of packages associated with a property. Packages here define a group of features that a property has the ability to utilize or access. By invoking this API method, developers will get a comprehensive view of the feature sets that are available and active for a specific property. The getPackages method boasts a seamless execution that offers essential information, vital in enhancing property management, understanding available functionalities and ultimately, optimizing user experience.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_packages_response import GetPackagesResponse
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
    api_instance = cloudbeds_pms_v1_3.PackageApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getPackages
        api_response = api_instance.get_packages_get(property_id=property_id)
        print("The response of PackageApi->get_packages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->get_packages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetPackagesResponse**](GetPackagesResponse.md)

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

