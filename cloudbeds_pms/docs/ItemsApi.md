# cloudbeds_pms.ItemsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_item_controller_index**](ItemsApi.md#custom_item_controller_index) | **GET** /item/v1/custom-items | Get a list of custom items for a specific property.
[**item_controller_create_items**](ItemsApi.md#item_controller_create_items) | **POST** /item/v1/items | Post one or more items to a reservation, house account, or group profile


# **custom_item_controller_index**
> CustomItemListResponseSchema custom_item_controller_index(x_property_id, limit=limit, offset=offset, filters=filters)

Get a list of custom items for a specific property.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.custom_item_list_response_schema import CustomItemListResponseSchema
from cloudbeds_pms.models.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema
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
    api_instance = cloudbeds_pms.ItemsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    filters = cloudbeds_pms.QueryParameterDynamicFilterSchema() # QueryParameterDynamicFilterSchema | This parameter should be formatted as a list of strings separated by ; (optional)

    try:
        # Get a list of custom items for a specific property.
        api_response = api_instance.custom_item_controller_index(x_property_id, limit=limit, offset=offset, filters=filters)
        print("The response of ItemsApi->custom_item_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->custom_item_controller_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **filters** | [**QueryParameterDynamicFilterSchema**](.md)| This parameter should be formatted as a list of strings separated by ; | [optional] 

### Return type

[**CustomItemListResponseSchema**](CustomItemListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of custom items. |  -  |
**400** | Bad Request response |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_controller_create_items**
> PostItemsResponseSchema item_controller_create_items(x_property_id, post_items_request_schema)

Post one or more items to a reservation, house account, or group profile

Adds items to a reservation, house account, or group profile. This endpoint supports batch operations, allowing multiple items to be posted in a single request. Each item can have associated payments and custom pricing.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.post_items_request_schema import PostItemsRequestSchema
from cloudbeds_pms.models.post_items_response_schema import PostItemsResponseSchema
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
    api_instance = cloudbeds_pms.ItemsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    post_items_request_schema = cloudbeds_pms.PostItemsRequestSchema() # PostItemsRequestSchema | Items to post with optional payment information

    try:
        # Post one or more items to a reservation, house account, or group profile
        api_response = api_instance.item_controller_create_items(x_property_id, post_items_request_schema)
        print("The response of ItemsApi->item_controller_create_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->item_controller_create_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **post_items_request_schema** | [**PostItemsRequestSchema**](PostItemsRequestSchema.md)| Items to post with optional payment information | 

### Return type

[**PostItemsResponseSchema**](PostItemsResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Items successfully posted |  -  |
**400** | Bad request - invalid parameters or validation errors |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - reservation, house account, or group not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

