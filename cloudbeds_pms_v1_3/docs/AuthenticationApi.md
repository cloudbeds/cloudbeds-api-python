# cloudbeds_pms_v1_3.AuthenticationApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token_post**](AuthenticationApi.md#access_token_post) | **POST** /access_token | access_token
[**oauth_metadata_get**](AuthenticationApi.md#oauth_metadata_get) | **GET** /oauth/metadata | metadata
[**userinfo_get**](AuthenticationApi.md#userinfo_get) | **GET** /userinfo | userinfo


# **access_token_post**
> PostAccessTokenResponse access_token_post(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)

access_token

Query the authorization server for an access token used to access property resources.</br> If the automatic delivery method for API keys is used, the grant type `urn:ietf:params:oauth:grant-type:api-key` needs to be used to request an API key. This grant type requires `grant_type=urn:ietf:params:oauth:grant-type:api-key`, `client_id`, `client_secret`, `redirect_uri` and `code`.</br> For OAuth 2.0., two different grant types (`authorization_code`, `refresh_token`) are supported. Authorization code grant type requires `grant_type=authorization_code`, `client_id`, `client_secret`, `redirect_uri`, `code`. Refresh token grant type requires `grant_type=refresh_token`, `client_id`, `client_secret`, `refresh_token`.</br> Read the [Authentication guide](https://integrations.cloudbeds.com/hc/en-us/sections/14731510501915-Authentication) for implementation tips, user flows and testing advice.

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_access_token_response import PostAccessTokenResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.AuthenticationApi(api_client)
    grant_type = 'grant_type_example' # str | The OAuth2 grant type. (optional)
    client_id = 'client_id_example' # str | The client identifier. Each client must be provisioned an identifier. (optional)
    client_secret = 'client_secret_example' # str | The client secret. Each client must be provisioned a secret. (optional)
    redirect_uri = 'redirect_uri_example' # str | The client pre-configured redirect URI. (Required for grant type 'authorization_code' and 'urn:ietf:params:oauth:grant-type:api-key'). (optional)
    code = 'code_example' # str | An authorization code provisioned by /oauth (Required for grant type 'authorization_code' and 'urn:ietf:params:oauth:grant-type:api-key'). (optional)
    refresh_token = 'refresh_token_example' # str | A refresh token to renew an access_token (Required for grant type 'refresh_token' only). (optional)

    try:
        # access_token
        api_response = api_instance.access_token_post(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
        print("The response of AuthenticationApi->access_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->access_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The OAuth2 grant type. | [optional] 
 **client_id** | **str**| The client identifier. Each client must be provisioned an identifier. | [optional] 
 **client_secret** | **str**| The client secret. Each client must be provisioned a secret. | [optional] 
 **redirect_uri** | **str**| The client pre-configured redirect URI. (Required for grant type &#39;authorization_code&#39; and &#39;urn:ietf:params:oauth:grant-type:api-key&#39;). | [optional] 
 **code** | **str**| An authorization code provisioned by /oauth (Required for grant type &#39;authorization_code&#39; and &#39;urn:ietf:params:oauth:grant-type:api-key&#39;). | [optional] 
 **refresh_token** | **str**| A refresh token to renew an access_token (Required for grant type &#39;refresh_token&#39; only). | [optional] 

### Return type

[**PostAccessTokenResponse**](PostAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_metadata_get**
> GetMetadataResponse oauth_metadata_get()

metadata

In the context of properties being distributed across multiple localizations, this endpoint serves to retrieve the precise location of the property associated with the provided access token. Further information can be found in the [Authentication guide](https://integrations.cloudbeds.com/hc/en-us/sections/14731510501915-Authentication).

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_metadata_response import GetMetadataResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.AuthenticationApi(api_client)

    try:
        # metadata
        api_response = api_instance.oauth_metadata_get()
        print("The response of AuthenticationApi->oauth_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_metadata_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetadataResponse**](GetMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userinfo_get**
> GetUserinfoResponse userinfo_get(property_id=property_id, role_details=role_details)

userinfo

Returns information on user who authorized connection

### Example


```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_userinfo_response import GetUserinfoResponse
from cloudbeds_pms_v1_3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloudbeds.com/api/v1.3
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudbeds_pms_v1_3.Configuration(
    host = "https://api.cloudbeds.com/api/v1.3"
)


# Enter a context with an instance of the API client
with cloudbeds_pms_v1_3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudbeds_pms_v1_3.AuthenticationApi(api_client)
    property_id = 'property_id_example' # str | Specify a property ID when using role_details (optional)
    role_details = True # bool | Specify whether to include role and acl details of the user. (optional)

    try:
        # userinfo
        api_response = api_instance.userinfo_get(property_id=property_id, role_details=role_details)
        print("The response of AuthenticationApi->userinfo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->userinfo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Specify a property ID when using role_details | [optional] 
 **role_details** | **bool**| Specify whether to include role and acl details of the user. | [optional] 

### Return type

[**GetUserinfoResponse**](GetUserinfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

