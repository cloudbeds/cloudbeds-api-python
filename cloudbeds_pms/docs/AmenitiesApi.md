# cloudbeds_pms.AmenitiesApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amenity_catalog_controller_get_amenity_catalog**](AmenitiesApi.md#amenity_catalog_controller_get_amenity_catalog) | **GET** /amenities/v1/catalogs/amenities | Get amenity catalog
[**amenity_catalog_controller_get_amenity_category_catalog**](AmenitiesApi.md#amenity_catalog_controller_get_amenity_category_catalog) | **GET** /amenities/v1/catalogs/categories | Get amenity category catalog
[**property_amenity_controller_get_property_amenities**](AmenitiesApi.md#property_amenity_controller_get_property_amenities) | **GET** /amenities/v1/properties/{propertyId}/amenities | Get property amenities
[**property_amenity_controller_update_property_amenities**](AmenitiesApi.md#property_amenity_controller_update_property_amenities) | **PUT** /amenities/v1/properties/{propertyId}/amenities | Update property amenities
[**room_amenity_controller_get_property_rooms_amenities**](AmenitiesApi.md#room_amenity_controller_get_property_rooms_amenities) | **GET** /amenities/v1/properties/{propertyId}/room-amenities | Get amenities for all rooms in a property
[**room_amenity_controller_get_room_amenities**](AmenitiesApi.md#room_amenity_controller_get_room_amenities) | **GET** /amenities/v1/properties/{propertyId}/rooms/{roomId}/amenities | Get room amenities
[**room_amenity_controller_update_property_rooms_amenities**](AmenitiesApi.md#room_amenity_controller_update_property_rooms_amenities) | **PUT** /amenities/v1/properties/{propertyId}/room-amenities | Update amenities for multiple rooms
[**room_amenity_controller_update_room_amenities**](AmenitiesApi.md#room_amenity_controller_update_room_amenities) | **PUT** /amenities/v1/properties/{propertyId}/rooms/{roomId}/amenities | Update room amenities


# **amenity_catalog_controller_get_amenity_catalog**
> GetAmenityCatalogResponseSchema amenity_catalog_controller_get_amenity_catalog(x_property_id, scope, accept_language=accept_language)

Get amenity catalog

Returns the complete list of amenities available for the specified scope (property or room) with their translated names and category codes.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.get_amenity_catalog_response_schema import GetAmenityCatalogResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    scope = 'property' # str | The scope of amenities to retrieve
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)

    try:
        # Get amenity catalog
        api_response = api_instance.amenity_catalog_controller_get_amenity_catalog(x_property_id, scope, accept_language=accept_language)
        print("The response of AmenitiesApi->amenity_catalog_controller_get_amenity_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->amenity_catalog_controller_get_amenity_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **scope** | **str**| The scope of amenities to retrieve | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 

### Return type

[**GetAmenityCatalogResponseSchema**](GetAmenityCatalogResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of amenities in the catalog for the requested scope. |  -  |
**400** | Invalid or missing scope parameter |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amenity_catalog_controller_get_amenity_category_catalog**
> GetAmenityCategoryCatalogResponseSchema amenity_catalog_controller_get_amenity_category_catalog(x_property_id, scope, accept_language=accept_language)

Get amenity category catalog

Returns the complete list of amenity categories available for the specified scope (property or room) with their translated names.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.get_amenity_category_catalog_response_schema import GetAmenityCategoryCatalogResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    scope = 'property' # str | The scope of amenities to retrieve
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)

    try:
        # Get amenity category catalog
        api_response = api_instance.amenity_catalog_controller_get_amenity_category_catalog(x_property_id, scope, accept_language=accept_language)
        print("The response of AmenitiesApi->amenity_catalog_controller_get_amenity_category_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->amenity_catalog_controller_get_amenity_category_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **scope** | **str**| The scope of amenities to retrieve | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 

### Return type

[**GetAmenityCategoryCatalogResponseSchema**](GetAmenityCategoryCatalogResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of amenity categories in the catalog for the requested scope. |  -  |
**400** | Invalid or missing scope parameter |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden response |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_amenity_controller_get_property_amenities**
> GetPropertyAmenitiesResponseSchema property_amenity_controller_get_property_amenities(property_id, accept_language=accept_language)

Get property amenities

Retrieve the complete set of active property amenities.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.get_property_amenities_response_schema import GetPropertyAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)

    try:
        # Get property amenities
        api_response = api_instance.property_amenity_controller_get_property_amenities(property_id, accept_language=accept_language)
        print("The response of AmenitiesApi->property_amenity_controller_get_property_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->property_amenity_controller_get_property_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 

### Return type

[**GetPropertyAmenitiesResponseSchema**](GetPropertyAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Property amenities retrieved successfully. |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_amenity_controller_update_property_amenities**
> UpdatePropertyAmenitiesResponseSchema property_amenity_controller_update_property_amenities(property_id, accept_language=accept_language, update_property_amenities_request_schema=update_property_amenities_request_schema)

Update property amenities

Replace the complete set of active property amenities in a single atomic transaction.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.update_property_amenities_request_schema import UpdatePropertyAmenitiesRequestSchema
from cloudbeds_pms.models.update_property_amenities_response_schema import UpdatePropertyAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)
    update_property_amenities_request_schema = cloudbeds_pms.UpdatePropertyAmenitiesRequestSchema() # UpdatePropertyAmenitiesRequestSchema | List of amenity codes to set for the property. (optional)

    try:
        # Update property amenities
        api_response = api_instance.property_amenity_controller_update_property_amenities(property_id, accept_language=accept_language, update_property_amenities_request_schema=update_property_amenities_request_schema)
        print("The response of AmenitiesApi->property_amenity_controller_update_property_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->property_amenity_controller_update_property_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 
 **update_property_amenities_request_schema** | [**UpdatePropertyAmenitiesRequestSchema**](UpdatePropertyAmenitiesRequestSchema.md)| List of amenity codes to set for the property. | [optional] 

### Return type

[**UpdatePropertyAmenitiesResponseSchema**](UpdatePropertyAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Property amenities updated successfully. |  -  |
**400** | Validation error - invalid amenity codes |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **room_amenity_controller_get_property_rooms_amenities**
> GetPropertyRoomsAmenitiesResponseSchema room_amenity_controller_get_property_rooms_amenities(property_id, accept_language=accept_language)

Get amenities for all rooms in a property

Retrieve the complete set of active amenities for all rooms in a property.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.get_property_rooms_amenities_response_schema import GetPropertyRoomsAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)

    try:
        # Get amenities for all rooms in a property
        api_response = api_instance.room_amenity_controller_get_property_rooms_amenities(property_id, accept_language=accept_language)
        print("The response of AmenitiesApi->room_amenity_controller_get_property_rooms_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->room_amenity_controller_get_property_rooms_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 

### Return type

[**GetPropertyRoomsAmenitiesResponseSchema**](GetPropertyRoomsAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room amenities retrieved successfully. |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **room_amenity_controller_get_room_amenities**
> GetRoomAmenitiesResponseSchema room_amenity_controller_get_room_amenities(room_id, property_id, accept_language=accept_language)

Get room amenities

Retrieve the complete set of active room amenities.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.get_room_amenities_response_schema import GetRoomAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    room_id = 12345 # int | The room id
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)

    try:
        # Get room amenities
        api_response = api_instance.room_amenity_controller_get_room_amenities(room_id, property_id, accept_language=accept_language)
        print("The response of AmenitiesApi->room_amenity_controller_get_room_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->room_amenity_controller_get_room_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The room id | 
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 

### Return type

[**GetRoomAmenitiesResponseSchema**](GetRoomAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room amenities retrieved successfully. |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property or room not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **room_amenity_controller_update_property_rooms_amenities**
> UpdatePropertyRoomsAmenitiesResponseSchema room_amenity_controller_update_property_rooms_amenities(property_id, accept_language=accept_language, update_property_rooms_amenities_request_schema=update_property_rooms_amenities_request_schema)

Update amenities for multiple rooms

Replace the complete set of active amenities for multiple rooms in a single atomic transaction.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.update_property_rooms_amenities_request_schema import UpdatePropertyRoomsAmenitiesRequestSchema
from cloudbeds_pms.models.update_property_rooms_amenities_response_schema import UpdatePropertyRoomsAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)
    update_property_rooms_amenities_request_schema = cloudbeds_pms.UpdatePropertyRoomsAmenitiesRequestSchema() # UpdatePropertyRoomsAmenitiesRequestSchema | List of rooms with amenity codes to set. (optional)

    try:
        # Update amenities for multiple rooms
        api_response = api_instance.room_amenity_controller_update_property_rooms_amenities(property_id, accept_language=accept_language, update_property_rooms_amenities_request_schema=update_property_rooms_amenities_request_schema)
        print("The response of AmenitiesApi->room_amenity_controller_update_property_rooms_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->room_amenity_controller_update_property_rooms_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 
 **update_property_rooms_amenities_request_schema** | [**UpdatePropertyRoomsAmenitiesRequestSchema**](UpdatePropertyRoomsAmenitiesRequestSchema.md)| List of rooms with amenity codes to set. | [optional] 

### Return type

[**UpdatePropertyRoomsAmenitiesResponseSchema**](UpdatePropertyRoomsAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room amenities updated successfully. |  -  |
**400** | Validation error - invalid amenity codes or room IDs |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property or room not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **room_amenity_controller_update_room_amenities**
> UpdateRoomAmenitiesResponseSchema room_amenity_controller_update_room_amenities(room_id, property_id, accept_language=accept_language, update_room_amenities_request_schema=update_room_amenities_request_schema)

Update room amenities

Replace the complete set of active room amenities in a single atomic transaction.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.update_room_amenities_request_schema import UpdateRoomAmenitiesRequestSchema
from cloudbeds_pms.models.update_room_amenities_response_schema import UpdateRoomAmenitiesResponseSchema
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
    api_instance = cloudbeds_pms.AmenitiesApi(api_client)
    room_id = 12345 # int | The room id
    property_id = 1 # int | The property ID
    accept_language = 'es-ES, en;q=0.8' # str | RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q=0.8). (optional)
    update_room_amenities_request_schema = cloudbeds_pms.UpdateRoomAmenitiesRequestSchema() # UpdateRoomAmenitiesRequestSchema | List of amenity codes to set for the room. (optional)

    try:
        # Update room amenities
        api_response = api_instance.room_amenity_controller_update_room_amenities(room_id, property_id, accept_language=accept_language, update_room_amenities_request_schema=update_room_amenities_request_schema)
        print("The response of AmenitiesApi->room_amenity_controller_update_room_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->room_amenity_controller_update_room_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The room id | 
 **property_id** | **int**| The property ID | 
 **accept_language** | **str**| RFC 5646 language preferences used for negotiation (e.g. es-ES, en;q&#x3D;0.8). | [optional] 
 **update_room_amenities_request_schema** | [**UpdateRoomAmenitiesRequestSchema**](UpdateRoomAmenitiesRequestSchema.md)| List of amenity codes to set for the room. | [optional] 

### Return type

[**UpdateRoomAmenitiesResponseSchema**](UpdateRoomAmenitiesResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room amenities updated successfully. |  -  |
**400** | Validation error - invalid amenity codes |  -  |
**401** | Unauthorized response |  -  |
**403** | Forbidden - missing required permissions |  -  |
**404** | Property or room not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

