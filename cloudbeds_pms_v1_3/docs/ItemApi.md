# cloudbeds_pms_v1_3.ItemApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_custom_item_post**](ItemApi.md#append_custom_item_post) | **POST** /appendCustomItem | appendCustomItem
[**delete_item_from_reservation_delete**](ItemApi.md#delete_item_from_reservation_delete) | **DELETE** /deleteItemFromReservation | deleteItemFromReservation
[**get_item_categories_get**](ItemApi.md#get_item_categories_get) | **GET** /getItemCategories | getItemCategories
[**get_item_get**](ItemApi.md#get_item_get) | **GET** /getItem | getItem
[**get_items_get**](ItemApi.md#get_items_get) | **GET** /getItems | getItems
[**post_custom_item_post**](ItemApi.md#post_custom_item_post) | **POST** /postCustomItem | postCustomItem
[**post_item_category_post**](ItemApi.md#post_item_category_post) | **POST** /postItemCategory | postItemCategory
[**post_item_post**](ItemApi.md#post_item_post) | **POST** /postItem | postItem
[**post_item_to_reservation_post**](ItemApi.md#post_item_to_reservation_post) | **POST** /postItemToReservation | postItemToReservation
[**post_items_to_inventory_post**](ItemApi.md#post_items_to_inventory_post) | **POST** /postItemsToInventory | postItemsToInventory
[**post_void_item_post**](ItemApi.md#post_void_item_post) | **POST** /postVoidItem | postVoidItem
[**put_item_to_inventory_put**](ItemApi.md#put_item_to_inventory_put) | **PUT** /putItemToInventory | putItemToInventory


# **append_custom_item_post**
> PostAppendCustomItemResponse append_custom_item_post(property_id=property_id, reservation_id=reservation_id, reference_id=reference_id, sub_reservation_id=sub_reservation_id, room_id=room_id, items=items, sale_date=sale_date, guest_id=guest_id, guest_name=guest_name, payments=payments, item_paid=item_paid)

appendCustomItem

Append single, or multiple, custom items and their associated payments to a existing one in a Reservation.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_append_custom_item_response import PostAppendCustomItemResponse
from cloudbeds_pms_v1_3.models.post_custom_item_request_items_inner import PostCustomItemRequestItemsInner
from cloudbeds_pms_v1_3.models.post_custom_item_request_payments_inner import PostCustomItemRequestPaymentsInner
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier. Required if no houseAccountID is provided. (optional)
    reference_id = 'reference_id_example' # str | partner's transaction reference. If exist then Cloudbeds will prevent adding of duplicates (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier (optional)
    room_id = 'room_id_example' # str | Room identifier (Ignored if subReservationID exist) (optional)
    items = [cloudbeds_pms_v1_3.PostCustomItemRequestItemsInner()] # List[PostCustomItemRequestItemsInner] | list of items will be posted (optional)
    sale_date = '2013-10-20T19:20:30+01:00' # datetime | posting date (optional)
    guest_id = 'guest_id_example' # str | Guest identifier (optional)
    guest_name = 'guest_name_example' # str | (Ignored if guestID exist) (optional)
    payments = [cloudbeds_pms_v1_3.PostCustomItemRequestPaymentsInner()] # List[PostCustomItemRequestPaymentsInner] | list of payments If the item is already paid (optional)
    item_paid = False # bool | If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. (Ignored if payments array exist) (optional) (default to False)

    try:
        # appendCustomItem
        api_response = api_instance.append_custom_item_post(property_id=property_id, reservation_id=reservation_id, reference_id=reference_id, sub_reservation_id=sub_reservation_id, room_id=room_id, items=items, sale_date=sale_date, guest_id=guest_id, guest_name=guest_name, payments=payments, item_paid=item_paid)
        print("The response of ItemApi->append_custom_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->append_custom_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier. Required if no houseAccountID is provided. | [optional] 
 **reference_id** | **str**| partner&#39;s transaction reference. If exist then Cloudbeds will prevent adding of duplicates | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier | [optional] 
 **room_id** | **str**| Room identifier (Ignored if subReservationID exist) | [optional] 
 **items** | [**List[PostCustomItemRequestItemsInner]**](PostCustomItemRequestItemsInner.md)| list of items will be posted | [optional] 
 **sale_date** | **datetime**| posting date | [optional] 
 **guest_id** | **str**| Guest identifier | [optional] 
 **guest_name** | **str**| (Ignored if guestID exist) | [optional] 
 **payments** | [**List[PostCustomItemRequestPaymentsInner]**](PostCustomItemRequestPaymentsInner.md)| list of payments If the item is already paid | [optional] 
 **item_paid** | **bool**| If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. (Ignored if payments array exist) | [optional] [default to False]

### Return type

[**PostAppendCustomItemResponse**](PostAppendCustomItemResponse.md)

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

# **delete_item_from_reservation_delete**
> DeleteItemFromReservationResponse delete_item_from_reservation_delete(reservation_id, sold_product_id)

deleteItemFromReservation

Deletes the itemID transaction from the specified reservationID. If payments were sent in calls [postItem](https://api.cloudbeds.com/api/v1.1/docs/#api-Item-postItem) or [postCustomItem](https://api.cloudbeds.com/api/v1.1/docs/#api-Item-postCustomItem), they will be deleted too.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_item_from_reservation_response import DeleteItemFromReservationResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation identifier
    sold_product_id = 'sold_product_id_example' # str | Item identifier

    try:
        # deleteItemFromReservation
        api_response = api_instance.delete_item_from_reservation_delete(reservation_id, sold_product_id)
        print("The response of ItemApi->delete_item_from_reservation_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->delete_item_from_reservation_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation identifier | 
 **sold_product_id** | **str**| Item identifier | 

### Return type

[**DeleteItemFromReservationResponse**](DeleteItemFromReservationResponse.md)

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

# **get_item_categories_get**
> GetItemCategoriesResponse get_item_categories_get(property_id=property_id)

getItemCategories

Gets the item category list

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_item_categories_response import GetItemCategoriesResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getItemCategories
        api_response = api_instance.get_item_categories_get(property_id=property_id)
        print("The response of ItemApi->get_item_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->get_item_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetItemCategoriesResponse**](GetItemCategoriesResponse.md)

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

# **get_item_get**
> GetItemResponse get_item_get(item_id, property_id=property_id)

getItem

Gets the details for the one itemID<br /> <sup>1</sup> only if data.stockInventory = true<br> <sup>2</sup> Taxes, fees and totals will show up only if an item has assigned tax or fee.<br>

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_item_response import GetItemResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    item_id = 'item_id_example' # str | Item identifier
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getItem
        api_response = api_instance.get_item_get(item_id, property_id=property_id)
        print("The response of ItemApi->get_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->get_item_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item identifier | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetItemResponse**](GetItemResponse.md)

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

# **get_items_get**
> GetItemsResponse get_items_get(property_id=property_id, item_category_id=item_category_id)

getItems

Gets all the items and their prices the hotel has created in myfrontdesk<br> <sup>1</sup> only if data.stockInventory = true<br> <sup>2</sup> Taxes, fees and totals will show up only if an item has assigned tax or fee.<br>

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_items_response import GetItemsResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    item_category_id = 'item_category_id_example' # str | Category identifier (optional)

    try:
        # getItems
        api_response = api_instance.get_items_get(property_id=property_id, item_category_id=item_category_id)
        print("The response of ItemApi->get_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->get_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **item_category_id** | **str**| Category identifier | [optional] 

### Return type

[**GetItemsResponse**](GetItemsResponse.md)

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

# **post_custom_item_post**
> PostCustomItemResponse post_custom_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, reference_id=reference_id, sub_reservation_id=sub_reservation_id, room_id=room_id, items=items, sale_date=sale_date, guest_id=guest_id, guest_name=guest_name, payments=payments, item_paid=item_paid)

postCustomItem

Adds single, or multiple, custom items and their associated payments to a Reservation or House Account as a single transaction.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_custom_item_request_items_inner import PostCustomItemRequestItemsInner
from cloudbeds_pms_v1_3.models.post_custom_item_request_payments_inner import PostCustomItemRequestPaymentsInner
from cloudbeds_pms_v1_3.models.post_custom_item_response import PostCustomItemResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier. Required if no houseAccountID or groupCode is provided. (optional)
    house_account_id = 'house_account_id_example' # str | House account identifier. Required if no reservationID or groupCode is provided. (optional)
    group_code = 'group_code_example' # str | Group identifier. Required if no reservationID or houseAccountID is provided. (optional)
    reference_id = 'reference_id_example' # str | partner's transaction reference. If exist then Cloudbeds will prevent adding of duplicates (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier (optional)
    room_id = 'room_id_example' # str | Room identifier (Ignored if subReservationID exist) (optional)
    items = [cloudbeds_pms_v1_3.PostCustomItemRequestItemsInner()] # List[PostCustomItemRequestItemsInner] | list of items will be posted (optional)
    sale_date = '2013-10-20T19:20:30+01:00' # datetime | posting date (optional)
    guest_id = 'guest_id_example' # str | Guest identifier (optional)
    guest_name = 'guest_name_example' # str | (Ignored if guestID exist) (optional)
    payments = [cloudbeds_pms_v1_3.PostCustomItemRequestPaymentsInner()] # List[PostCustomItemRequestPaymentsInner] | list of payments If the item is already paid (optional)
    item_paid = False # bool | If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. (Ignored if payments array exist) (optional) (default to False)

    try:
        # postCustomItem
        api_response = api_instance.post_custom_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, reference_id=reference_id, sub_reservation_id=sub_reservation_id, room_id=room_id, items=items, sale_date=sale_date, guest_id=guest_id, guest_name=guest_name, payments=payments, item_paid=item_paid)
        print("The response of ItemApi->post_custom_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_custom_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier. Required if no houseAccountID or groupCode is provided. | [optional] 
 **house_account_id** | **str**| House account identifier. Required if no reservationID or groupCode is provided. | [optional] 
 **group_code** | **str**| Group identifier. Required if no reservationID or houseAccountID is provided. | [optional] 
 **reference_id** | **str**| partner&#39;s transaction reference. If exist then Cloudbeds will prevent adding of duplicates | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier | [optional] 
 **room_id** | **str**| Room identifier (Ignored if subReservationID exist) | [optional] 
 **items** | [**List[PostCustomItemRequestItemsInner]**](PostCustomItemRequestItemsInner.md)| list of items will be posted | [optional] 
 **sale_date** | **datetime**| posting date | [optional] 
 **guest_id** | **str**| Guest identifier | [optional] 
 **guest_name** | **str**| (Ignored if guestID exist) | [optional] 
 **payments** | [**List[PostCustomItemRequestPaymentsInner]**](PostCustomItemRequestPaymentsInner.md)| list of payments If the item is already paid | [optional] 
 **item_paid** | **bool**| If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. (Ignored if payments array exist) | [optional] [default to False]

### Return type

[**PostCustomItemResponse**](PostCustomItemResponse.md)

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

# **post_item_category_post**
> PostItemCategoryResponse post_item_category_post(property_id=property_id, category_name=category_name, category_code=category_code, item_id=item_id, category_color=category_color)

postItemCategory

Adds new items category

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_item_category_response import PostItemCategoryResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    category_name = 'category_name_example' # str | Category name (optional)
    category_code = 'category_code_example' # str | Category code (optional)
    item_id = [56] # List[int] | Existing ItemIDs to reassign to new category (optional)
    category_color = '#ccc' # str | Category color (like #3b7be7) (optional) (default to '#ccc')

    try:
        # postItemCategory
        api_response = api_instance.post_item_category_post(property_id=property_id, category_name=category_name, category_code=category_code, item_id=item_id, category_color=category_color)
        print("The response of ItemApi->post_item_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_item_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **category_name** | **str**| Category name | [optional] 
 **category_code** | **str**| Category code | [optional] 
 **item_id** | [**List[int]**](int.md)| Existing ItemIDs to reassign to new category | [optional] 
 **category_color** | **str**| Category color (like #3b7be7) | [optional] [default to &#39;#ccc&#39;]

### Return type

[**PostItemCategoryResponse**](PostItemCategoryResponse.md)

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

# **post_item_post**
> PostItemResponse post_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, sub_reservation_id=sub_reservation_id, item_id=item_id, item_quantity=item_quantity, item_price=item_price, item_note=item_note, item_paid=item_paid, sale_date=sale_date, payments=payments)

postItem

Adds an item either to a reservation or to a house account.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_item_response import PostItemResponse
from cloudbeds_pms_v1_3.models.post_item_to_reservation_request_payments_inner import PostItemToReservationRequestPaymentsInner
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier. Required if no houseAccountID or groupCode is provided. (optional)
    house_account_id = 'house_account_id_example' # str | House account identifier. Required if no reservationID or groupCode is provided. (optional)
    group_code = 'group_code_example' # str | Group identifier. Required if no reservationID or houseAccountID is provided. (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation identifier. (optional)
    item_id = 'item_id_example' # str | Item identifier (optional)
    item_quantity = 56 # int | Items quantity (optional)
    item_price = 'item_price_example' # str | Item price, if not sent, items registered price will be used (optional)
    item_note = 'item_note_example' # str | Item note (optional)
    item_paid = False # bool | If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. If payments is set, itemPaid is ignored. (optional) (default to False)
    sale_date = '2013-10-20T19:20:30+01:00' # datetime | posting date (optional)
    payments = [cloudbeds_pms_v1_3.PostItemToReservationRequestPaymentsInner()] # List[PostItemToReservationRequestPaymentsInner] | list of payments If the item is already paid (optional)

    try:
        # postItem
        api_response = api_instance.post_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, sub_reservation_id=sub_reservation_id, item_id=item_id, item_quantity=item_quantity, item_price=item_price, item_note=item_note, item_paid=item_paid, sale_date=sale_date, payments=payments)
        print("The response of ItemApi->post_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier. Required if no houseAccountID or groupCode is provided. | [optional] 
 **house_account_id** | **str**| House account identifier. Required if no reservationID or groupCode is provided. | [optional] 
 **group_code** | **str**| Group identifier. Required if no reservationID or houseAccountID is provided. | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation identifier. | [optional] 
 **item_id** | **str**| Item identifier | [optional] 
 **item_quantity** | **int**| Items quantity | [optional] 
 **item_price** | **str**| Item price, if not sent, items registered price will be used | [optional] 
 **item_note** | **str**| Item note | [optional] 
 **item_paid** | **bool**| If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. If payments is set, itemPaid is ignored. | [optional] [default to False]
 **sale_date** | **datetime**| posting date | [optional] 
 **payments** | [**List[PostItemToReservationRequestPaymentsInner]**](PostItemToReservationRequestPaymentsInner.md)| list of payments If the item is already paid | [optional] 

### Return type

[**PostItemResponse**](PostItemResponse.md)

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

# **post_item_to_reservation_post**
> PostItemToReservationResponse post_item_to_reservation_post(property_id=property_id, reservation_id=reservation_id, item_id=item_id, item_quantity=item_quantity, item_price=item_price, item_note=item_note, item_paid=item_paid, sale_date=sale_date, payments=payments)

postItemToReservation

Adds an item to a reservation.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_item_to_reservation_request_payments_inner import PostItemToReservationRequestPaymentsInner
from cloudbeds_pms_v1_3.models.post_item_to_reservation_response import PostItemToReservationResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    item_id = 'item_id_example' # str | Item identifier (optional)
    item_quantity = 56 # int | Items quantity (optional)
    item_price = 'item_price_example' # str | Item price, if not sent, items registered price will be used (optional)
    item_note = 'item_note_example' # str | Item note (optional)
    item_paid = False # bool | If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. If payments is set, itemPaid is ignored. (optional) (default to False)
    sale_date = '2013-10-20' # date | posting date (optional)
    payments = [cloudbeds_pms_v1_3.PostItemToReservationRequestPaymentsInner()] # List[PostItemToReservationRequestPaymentsInner] | list of payments If the item is already paid (optional)

    try:
        # postItemToReservation
        api_response = api_instance.post_item_to_reservation_post(property_id=property_id, reservation_id=reservation_id, item_id=item_id, item_quantity=item_quantity, item_price=item_price, item_note=item_note, item_paid=item_paid, sale_date=sale_date, payments=payments)
        print("The response of ItemApi->post_item_to_reservation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_item_to_reservation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **item_id** | **str**| Item identifier | [optional] 
 **item_quantity** | **int**| Items quantity | [optional] 
 **item_price** | **str**| Item price, if not sent, items registered price will be used | [optional] 
 **item_note** | **str**| Item note | [optional] 
 **item_paid** | **bool**| If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes and fees. If this is not the expected behavior, set to false, and register the operation manually. If payments is set, itemPaid is ignored. | [optional] [default to False]
 **sale_date** | **date**| posting date | [optional] 
 **payments** | [**List[PostItemToReservationRequestPaymentsInner]**](PostItemToReservationRequestPaymentsInner.md)| list of payments If the item is already paid | [optional] 

### Return type

[**PostItemToReservationResponse**](PostItemToReservationResponse.md)

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

# **post_items_to_inventory_post**
> PostItemsToInventoryResponse post_items_to_inventory_post(item=item)

postItemsToInventory

Adds new items batch<br /> ¹ only if item.stockInventory = true<br />

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_items_to_inventory_request_item import PostItemsToInventoryRequestItem
from cloudbeds_pms_v1_3.models.post_items_to_inventory_response import PostItemsToInventoryResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    item = cloudbeds_pms_v1_3.PostItemsToInventoryRequestItem() # PostItemsToInventoryRequestItem |  (optional)

    try:
        # postItemsToInventory
        api_response = api_instance.post_items_to_inventory_post(item=item)
        print("The response of ItemApi->post_items_to_inventory_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_items_to_inventory_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**PostItemsToInventoryRequestItem**](PostItemsToInventoryRequestItem.md)|  | [optional] 

### Return type

[**PostItemsToInventoryResponse**](PostItemsToInventoryResponse.md)

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

# **post_void_item_post**
> PostVoidItemResponse post_void_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, sold_product_id=sold_product_id)

postVoidItem

Voids the itemID transaction on the specified Reservation ID, House Account ID, or Group. If payments were sent in calls [postItem](https://developers.cloudbeds.com/reference/post_postitem) or [postCustomItem](https://developers.cloudbeds.com/reference/post_postcustomitem), they will be deleted too.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_void_item_response import PostVoidItemResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier. Required if no houseAccountID or groupCode is provided. (optional)
    house_account_id = 'house_account_id_example' # str | House Account identifier. Required if no reservationID or groupCode is provided. (optional)
    group_code = 'group_code_example' # str | Group identifier. Required if no reservationID or houseAccountID is provided. (optional)
    sold_product_id = 'sold_product_id_example' # str | Item identifier (optional)

    try:
        # postVoidItem
        api_response = api_instance.post_void_item_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_code=group_code, sold_product_id=sold_product_id)
        print("The response of ItemApi->post_void_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->post_void_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier. Required if no houseAccountID or groupCode is provided. | [optional] 
 **house_account_id** | **str**| House Account identifier. Required if no reservationID or groupCode is provided. | [optional] 
 **group_code** | **str**| Group identifier. Required if no reservationID or houseAccountID is provided. | [optional] 
 **sold_product_id** | **str**| Item identifier | [optional] 

### Return type

[**PostVoidItemResponse**](PostVoidItemResponse.md)

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

# **put_item_to_inventory_put**
> PutItemToInventoryResponse put_item_to_inventory_put(property_id=property_id, item_id=item_id, item_name=item_name, item_type=item_type, item_sku=item_sku, item_code=item_code, item_description=item_description, item_price=item_price, stock_inventory=stock_inventory, item_quantity=item_quantity, reorder_threshold=reorder_threshold, stop_sell_met=stop_sell_met, stop_sell=stop_sell)

putItemToInventory

Updates an item with information provided<br /> ¹ only if item.stockInventory = true<br />

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.put_item_to_inventory_response import PutItemToInventoryResponse
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
    api_instance = cloudbeds_pms_v1_3.ItemApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    item_id = 'item_id_example' # str | Item identifier (optional)
    item_name = 'item_name_example' # str | Item name (optional)
    item_type = 'item_type_example' # str | Item type (optional)
    item_sku = 'item_sku_example' # str | Item SKU. Will be generated if not set (optional)
    item_code = 'item_code_example' # str | Item code (optional)
    item_description = 'item_description_example' # str | Item description (optional)
    item_price = 3.4 # float | Item price (optional)
    stock_inventory = True # bool | Track stock inventory for this item (optional)
    item_quantity = 56 # int | ¹ Current amount of item available (optional)
    reorder_threshold = 56 # int | ¹ Quantity at which to reorder item (optional)
    stop_sell_met = True # bool | ¹ true - Whether item is at or below value set for stop-sell threshold. (optional)
    stop_sell = 56 # int | ¹ Quantity at which to stop selling product. (optional)

    try:
        # putItemToInventory
        api_response = api_instance.put_item_to_inventory_put(property_id=property_id, item_id=item_id, item_name=item_name, item_type=item_type, item_sku=item_sku, item_code=item_code, item_description=item_description, item_price=item_price, stock_inventory=stock_inventory, item_quantity=item_quantity, reorder_threshold=reorder_threshold, stop_sell_met=stop_sell_met, stop_sell=stop_sell)
        print("The response of ItemApi->put_item_to_inventory_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemApi->put_item_to_inventory_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **item_id** | **str**| Item identifier | [optional] 
 **item_name** | **str**| Item name | [optional] 
 **item_type** | **str**| Item type | [optional] 
 **item_sku** | **str**| Item SKU. Will be generated if not set | [optional] 
 **item_code** | **str**| Item code | [optional] 
 **item_description** | **str**| Item description | [optional] 
 **item_price** | **float**| Item price | [optional] 
 **stock_inventory** | **bool**| Track stock inventory for this item | [optional] 
 **item_quantity** | **int**| ¹ Current amount of item available | [optional] 
 **reorder_threshold** | **int**| ¹ Quantity at which to reorder item | [optional] 
 **stop_sell_met** | **bool**| ¹ true - Whether item is at or below value set for stop-sell threshold. | [optional] 
 **stop_sell** | **int**| ¹ Quantity at which to stop selling product. | [optional] 

### Return type

[**PutItemToInventoryResponse**](PutItemToInventoryResponse.md)

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

