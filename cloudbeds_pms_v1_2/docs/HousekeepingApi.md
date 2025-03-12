# cloudbeds_pms_v1_2.HousekeepingApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_housekeepers_get**](HousekeepingApi.md#get_housekeepers_get) | **GET** /getHousekeepers | getHousekeepers
[**get_housekeeping_status_get**](HousekeepingApi.md#get_housekeeping_status_get) | **GET** /getHousekeepingStatus | getHousekeepingStatus
[**post_housekeeper_post**](HousekeepingApi.md#post_housekeeper_post) | **POST** /postHousekeeper | postHousekeeper
[**post_housekeeping_assignment_post**](HousekeepingApi.md#post_housekeeping_assignment_post) | **POST** /postHousekeepingAssignment | postHousekeepingAssignment
[**post_housekeeping_status_post**](HousekeepingApi.md#post_housekeeping_status_post) | **POST** /postHousekeepingStatus | postHousekeepingStatus
[**put_housekeeper_put**](HousekeepingApi.md#put_housekeeper_put) | **PUT** /putHousekeeper | putHousekeeper


# **get_housekeepers_get**
> GetHousekeepersResponse get_housekeepers_get(property_id=property_id, page_number=page_number, page_size=page_size)

getHousekeepers

Returns a list of housekeepers ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_housekeepers_response import GetHousekeepersResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89). It can be omitted if the API key is single-property, or to get results from all properties on an association. (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 1000 (optional) (default to 100)

    try:
        # getHousekeepers
        api_response = api_instance.get_housekeepers_get(property_id=property_id, page_number=page_number, page_size=page_size)
        print("The response of HousekeepingApi->get_housekeepers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->get_housekeepers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89). It can be omitted if the API key is single-property, or to get results from all properties on an association. | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 1000 | [optional] [default to 100]

### Return type

[**GetHousekeepersResponse**](GetHousekeepersResponse.md)

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

# **get_housekeeping_status_get**
> GetHousekeepingStatusResponse get_housekeeping_status_get(property_id=property_id, room_type_ids=room_type_ids, housekeeper_ids=housekeeper_ids, room_condition=room_condition, room_occupied=room_occupied, page_number=page_number, page_size=page_size)

getHousekeepingStatus

Returns the current date's housekeeping information The housekeeping status is calculated basing on the set of fields roomOccupied | roomCondition | roomBlocked | vacantPickup | roomBlocked | refusedService The available statuses are: - Vacant and Dirty (VD): false | “dirty” | false | false | false | false - Occupied and Dirty (OD): true | “dirty” | false | false | false | false - Vacant and Clean (VC): false | “clean” | false | false | false | false - Occupied and Clean (OC): true | “clean” | false | false | false | false - Occupied and Clean Inspected (OCI): true | “inspected” | false | false | false | false - Vacant and Clean Inspected (VCI): false | “inspected” | false | false | false | false - Do Not Disturb (DND): if doNotDisturb is true - Refused Service (RS): if refusedService is true - Out of Order (OOO): if roomBlocked is true - Vacant and Pickup (VP): if vacantPickup is true

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_housekeeping_status_response import GetHousekeepingStatusResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_type_ids = 'room_type_ids_example' # str | Filter by room type ID. If more than one, send as comma-separated, i.e. 37,345,89 (optional)
    housekeeper_ids = 'housekeeper_ids_example' # str | Use this parameter to filter by housekeeper. If you need to specify multiple housekeepers, send their IDs as a comma-separated list (e.g., 37, 345, 89). To retrieve unassigned housekeepers, use the value 0. (optional)
    room_condition = 'room_condition_example' # str | Condition of room (optional)
    room_occupied = True # bool | Flag for current room occupation status (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 5000 (optional) (default to 100)

    try:
        # getHousekeepingStatus
        api_response = api_instance.get_housekeeping_status_get(property_id=property_id, room_type_ids=room_type_ids, housekeeper_ids=housekeeper_ids, room_condition=room_condition, room_occupied=room_occupied, page_number=page_number, page_size=page_size)
        print("The response of HousekeepingApi->get_housekeeping_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->get_housekeeping_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_type_ids** | **str**| Filter by room type ID. If more than one, send as comma-separated, i.e. 37,345,89 | [optional] 
 **housekeeper_ids** | **str**| Use this parameter to filter by housekeeper. If you need to specify multiple housekeepers, send their IDs as a comma-separated list (e.g., 37, 345, 89). To retrieve unassigned housekeepers, use the value 0. | [optional] 
 **room_condition** | **str**| Condition of room | [optional] 
 **room_occupied** | **bool**| Flag for current room occupation status | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 5000 | [optional] [default to 100]

### Return type

[**GetHousekeepingStatusResponse**](GetHousekeepingStatusResponse.md)

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

# **post_housekeeper_post**
> PostHousekeeperResponse post_housekeeper_post(property_id=property_id, name=name)

postHousekeeper

Add New Housekeeper

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_housekeeper_response import PostHousekeeperResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    name = 'name_example' # str | Housekeeper name (optional)

    try:
        # postHousekeeper
        api_response = api_instance.post_housekeeper_post(property_id=property_id, name=name)
        print("The response of HousekeepingApi->post_housekeeper_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->post_housekeeper_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **name** | **str**| Housekeeper name | [optional] 

### Return type

[**PostHousekeeperResponse**](PostHousekeeperResponse.md)

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

# **post_housekeeping_assignment_post**
> PostHousekeepingAssignmentResponse post_housekeeping_assignment_post(property_id=property_id, room_ids=room_ids, housekeeper_id=housekeeper_id)

postHousekeepingAssignment

Assign rooms (single or multiple) to an existing housekeeper

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_housekeeping_assignment_response import PostHousekeepingAssignmentResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_ids = 'room_ids_example' # str | List of room IDs comma-separated, i.e. 37,345,89 (optional)
    housekeeper_id = 'housekeeper_id_example' # str | Housekeeper ID. To designate a room as unassigned, simply set the value to 0. (optional)

    try:
        # postHousekeepingAssignment
        api_response = api_instance.post_housekeeping_assignment_post(property_id=property_id, room_ids=room_ids, housekeeper_id=housekeeper_id)
        print("The response of HousekeepingApi->post_housekeeping_assignment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->post_housekeeping_assignment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_ids** | **str**| List of room IDs comma-separated, i.e. 37,345,89 | [optional] 
 **housekeeper_id** | **str**| Housekeeper ID. To designate a room as unassigned, simply set the value to 0. | [optional] 

### Return type

[**PostHousekeepingAssignmentResponse**](PostHousekeepingAssignmentResponse.md)

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

# **post_housekeeping_status_post**
> PostHousekeepingStatusResponse post_housekeeping_status_post(property_id=property_id, room_id=room_id, room_condition=room_condition, do_not_disturb=do_not_disturb, room_comments=room_comments, refused_service=refused_service, vacant_pickup=vacant_pickup)

postHousekeepingStatus

Switches the current date's housekeeping status for a specific room ID to either clean or dirty The housekeeping status is calculated basing on the set of fields roomOccupied | roomCondition | roomBlocked | vacantPickup | roomBlocked | refusedService The available statuses are: - Vacant and Dirty (VD): false | “dirty” | false | false | false | false - Occupied and Dirty (OD): true | “dirty” | false | false | false | false - Vacant and Clean (VC): false | “clean” | false | false | false | false - Occupied and Clean (OC): true | “clean” | false | false | false | false - Occupied and Clean Inspected (OCI): true | “inspected” | false | false | false | false - Vacant and Clean Inspected (VCI): false | “inspected” | false | false | false | false - Do Not Disturb (DND): if doNotDisturb is true - Refused Service (RS): if refusedService is true - Out of Order (OOO): if roomBlocked is true - Vacant and Pickup (VP): if vacantPickup is true

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_housekeeping_status_response import PostHousekeepingStatusResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    room_id = 'room_id_example' # str | Room ID (optional)
    room_condition = 'room_condition_example' # str | New room condition. If no optional parameters are sent, will switch from current room condition. \\\"inspected\\\" status is available only if the property has the feature enabled. (optional)
    do_not_disturb = True # bool | New \\\"do not disturb\\\" status (optional)
    room_comments = 'room_comments_example' # str | New room comments. (optional)
    refused_service = True # bool | New \\\"refused service\\\" status (optional)
    vacant_pickup = True # bool | New \\\"vacant_pickup\\\" status (optional)

    try:
        # postHousekeepingStatus
        api_response = api_instance.post_housekeeping_status_post(property_id=property_id, room_id=room_id, room_condition=room_condition, do_not_disturb=do_not_disturb, room_comments=room_comments, refused_service=refused_service, vacant_pickup=vacant_pickup)
        print("The response of HousekeepingApi->post_housekeeping_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->post_housekeeping_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **room_id** | **str**| Room ID | [optional] 
 **room_condition** | **str**| New room condition. If no optional parameters are sent, will switch from current room condition. \\\&quot;inspected\\\&quot; status is available only if the property has the feature enabled. | [optional] 
 **do_not_disturb** | **bool**| New \\\&quot;do not disturb\\\&quot; status | [optional] 
 **room_comments** | **str**| New room comments. | [optional] 
 **refused_service** | **bool**| New \\\&quot;refused service\\\&quot; status | [optional] 
 **vacant_pickup** | **bool**| New \\\&quot;vacant_pickup\\\&quot; status | [optional] 

### Return type

[**PostHousekeepingStatusResponse**](PostHousekeepingStatusResponse.md)

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

# **put_housekeeper_put**
> PutHousekeeperResponse put_housekeeper_put(property_id=property_id, name=name, housekeeper_id=housekeeper_id)

putHousekeeper

Edit Housekeeper Details

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.put_housekeeper_response import PutHousekeeperResponse
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
    api_instance = cloudbeds_pms_v1_2.HousekeepingApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    name = 'name_example' # str | Housekeeper name (optional)
    housekeeper_id = 'housekeeper_id_example' # str | Housekeeper ID (optional)

    try:
        # putHousekeeper
        api_response = api_instance.put_housekeeper_put(property_id=property_id, name=name, housekeeper_id=housekeeper_id)
        print("The response of HousekeepingApi->put_housekeeper_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HousekeepingApi->put_housekeeper_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **name** | **str**| Housekeeper name | [optional] 
 **housekeeper_id** | **str**| Housekeeper ID | [optional] 

### Return type

[**PutHousekeeperResponse**](PutHousekeeperResponse.md)

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

