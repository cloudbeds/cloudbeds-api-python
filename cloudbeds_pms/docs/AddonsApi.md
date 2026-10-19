# cloudbeds_pms.AddonsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addon_controller_delete_reservation_addon**](AddonsApi.md#addon_controller_delete_reservation_addon) | **DELETE** /addons/v1/reservations/{reservationId}/addons/{soldAddonId} | Void an add-on on a reservation
[**addon_controller_get_addons**](AddonsApi.md#addon_controller_get_addons) | **GET** /addons/v1/addons | Retrieve property add-ons


# **addon_controller_delete_reservation_addon**
> object addon_controller_delete_reservation_addon(x_property_id, reservation_id, sold_addon_id)

Void an add-on on a reservation

Voids one add-on on a reservation, with its charge, taxes and fees, the same way the MFD UI does. Idempotent: voiding an already-voided add-on returns 204.

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
    api_instance = cloudbeds_pms.AddonsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    reservation_id = 'reservation_id_example' # str | The reservation ID, as returned by getReservation.
    sold_addon_id = 'sold_addon_id_example' # str | The add-on's soldProductID from reservationAddOnProducts in getReservation.

    try:
        # Void an add-on on a reservation
        api_response = api_instance.addon_controller_delete_reservation_addon(x_property_id, reservation_id, sold_addon_id)
        print("The response of AddonsApi->addon_controller_delete_reservation_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addon_controller_delete_reservation_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **reservation_id** | **str**| The reservation ID, as returned by getReservation. | 
 **sold_addon_id** | **str**| The add-on&#39;s soldProductID from reservationAddOnProducts in getReservation. | 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Add-on voided (or already voided - idempotent). |  -  |
**400** | Bad Request - soldAddonId is not a positive whole number |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**403** | Forbidden - Missing the write:item scope or access to the property |  -  |
**404** | Not found - no add-on with this ID on this reservation and property (ADDON_NOT_FOUND) |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addon_controller_get_addons**
> AddonsResponseSchema addon_controller_get_addons(x_property_id, limit=limit, offset=offset, filters=filters, accept_language=accept_language)

Retrieve property add-ons

Fetches list of Add-ons with basic information for a specific property

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.addons_response_schema import AddonsResponseSchema
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
    api_instance = cloudbeds_pms.AddonsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    limit = 100 # int | The maximum number of items to return in the response. Default is 100. (optional) (default to 100)
    offset = 0 # int | The number of items to skip before starting to collect the result set. Used for pagination. (optional) (default to 0)
    filters = cloudbeds_pms.QueryParameterDynamicFilterSchema() # QueryParameterDynamicFilterSchema | This parameter should be formatted as a list of strings separated by ; Use \\; for a literal semicolon inside a value. (optional)
    accept_language = 'accept_language_example' # str | The preferred language(s) for localized strings (e.g., en-US) (optional)

    try:
        # Retrieve property add-ons
        api_response = api_instance.addon_controller_get_addons(x_property_id, limit=limit, offset=offset, filters=filters, accept_language=accept_language)
        print("The response of AddonsApi->addon_controller_get_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addon_controller_get_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **limit** | **int**| The maximum number of items to return in the response. Default is 100. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. Used for pagination. | [optional] [default to 0]
 **filters** | [**QueryParameterDynamicFilterSchema**](.md)| This parameter should be formatted as a list of strings separated by ; Use \\; for a literal semicolon inside a value. | [optional] 
 **accept_language** | **str**| The preferred language(s) for localized strings (e.g., en-US) | [optional] 

### Return type

[**AddonsResponseSchema**](AddonsResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request - Invalid input parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

