# cloudbeds_pms_v1_3.PaymentApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_methods_get**](PaymentApi.md#get_payment_methods_get) | **GET** /getPaymentMethods | getPaymentMethods
[**get_payments_capabilities_get**](PaymentApi.md#get_payments_capabilities_get) | **GET** /getPaymentsCapabilities | getPaymentsCapabilities
[**get_payments_get**](PaymentApi.md#get_payments_get) | **GET** /getPayments | getPayments
[**get_pending_transactions_get**](PaymentApi.md#get_pending_transactions_get) | **GET** /getPendingTransactions | getPendingTransactions
[**get_transactions_get**](PaymentApi.md#get_transactions_get) | **GET** /getTransactions | getTransactions
[**post_charge_post**](PaymentApi.md#post_charge_post) | **POST** /postCharge | postCharge
[**post_credit_card_post**](PaymentApi.md#post_credit_card_post) | **POST** /postCreditCard | postCreditCard
[**post_custom_payment_method_post**](PaymentApi.md#post_custom_payment_method_post) | **POST** /postCustomPaymentMethod | postCustomPaymentMethod
[**post_payment_cash_post**](PaymentApi.md#post_payment_cash_post) | **POST** /postPaymentCash | postPaymentCash
[**post_payment_credit_card_post**](PaymentApi.md#post_payment_credit_card_post) | **POST** /postPaymentCreditCard | postPaymentCreditCard
[**post_payment_post**](PaymentApi.md#post_payment_post) | **POST** /postPayment | postPayment
[**post_void_payment_post**](PaymentApi.md#post_void_payment_post) | **POST** /postVoidPayment | postVoidPayment


# **get_payment_methods_get**
> GetPaymentMethodsResponse get_payment_methods_get(property_id=property_id, lang=lang)

getPaymentMethods

Get a list of active methods for a property, or list of properties

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_payment_methods_response import GetPaymentMethodsResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | ID for the property to be queried (optional)
    lang = en # str | Language that payment methods name should return (if available). (optional) (default to en)

    try:
        # getPaymentMethods
        api_response = api_instance.get_payment_methods_get(property_id=property_id, lang=lang)
        print("The response of PaymentApi->get_payment_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_methods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the property to be queried | [optional] 
 **lang** | **str**| Language that payment methods name should return (if available). | [optional] [default to en]

### Return type

[**GetPaymentMethodsResponse**](GetPaymentMethodsResponse.md)

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

# **get_payments_capabilities_get**
> GetPaymentsCapabilitiesResponse get_payments_capabilities_get(property_id=property_id)

getPaymentsCapabilities

Lists the payment capabilities of a given property

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_payments_capabilities_response import GetPaymentsCapabilitiesResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | ID for the property to be queried (optional)

    try:
        # getPaymentsCapabilities
        api_response = api_instance.get_payments_capabilities_get(property_id=property_id)
        print("The response of PaymentApi->get_payments_capabilities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payments_capabilities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the property to be queried | [optional] 

### Return type

[**GetPaymentsCapabilitiesResponse**](GetPaymentsCapabilitiesResponse.md)

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

# **get_payments_get**
> GetPaymentsResponse get_payments_get(reservation_id, house_account_id, guest_id, property_id=property_id, created_from=created_from, created_to=created_to, include_payment_allocation=include_payment_allocation, page_number=page_number, page_size=page_size)

getPayments

Get a list of transactions for a reservation/house account/guest, with its respective payment allocation<br /> ¹ one of these fields are required ² only if data.isAllocated = true (and includePaymentAllocation = true)

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_payments_response import GetPaymentsResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    reservation_id = 'reservation_id_example' # str | ¹ ID for the reservation to be queried.
    house_account_id = 'house_account_id_example' # str | ¹ ID for the house account to be queried.
    guest_id = 'guest_id_example' # str | ¹ ID for the guest to be queried.
    property_id = 'property_id_example' # str | Property ID (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Datetime (lower limit) to be queried. If not sent, and reservationID informed, will use reservation date. In other cases, current date -7 days is used. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Datetime (upper limit) to be queried. If not sent, and reservationID informed, will use check-out date. In other cases, current date is used. (optional)
    include_payment_allocation = False # bool | Adds payment allocation to response, when available. (optional) (default to False)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 100 # int | Page size (optional) (default to 100)

    try:
        # getPayments
        api_response = api_instance.get_payments_get(reservation_id, house_account_id, guest_id, property_id=property_id, created_from=created_from, created_to=created_to, include_payment_allocation=include_payment_allocation, page_number=page_number, page_size=page_size)
        print("The response of PaymentApi->get_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| ¹ ID for the reservation to be queried. | 
 **house_account_id** | **str**| ¹ ID for the house account to be queried. | 
 **guest_id** | **str**| ¹ ID for the guest to be queried. | 
 **property_id** | **str**| Property ID | [optional] 
 **created_from** | **datetime**| Datetime (lower limit) to be queried. If not sent, and reservationID informed, will use reservation date. In other cases, current date -7 days is used. | [optional] 
 **created_to** | **datetime**| Datetime (upper limit) to be queried. If not sent, and reservationID informed, will use check-out date. In other cases, current date is used. | [optional] 
 **include_payment_allocation** | **bool**| Adds payment allocation to response, when available. | [optional] [default to False]
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 100]

### Return type

[**GetPaymentsResponse**](GetPaymentsResponse.md)

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

# **get_pending_transactions_get**
> GetPendingTransactionsResponse get_pending_transactions_get(property_id=property_id, include_debit=include_debit, include_credit=include_credit, include_deleted=include_deleted, include_children=include_children, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id, guest_id=guest_id, house_account_id=house_account_id, transaction_ids=transaction_ids, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, created_from=created_from, created_to=created_to, page_number=page_number, page_size=page_size, sort_by=sort_by, order_by=order_by)

getPendingTransactions

Get a list of pending transactions for a property, or list of properties, for the date range specified. If no date range or reservation is specified, it will return the transactions for the last 7 days, unless stated otherwise.<br /> Please note that some reservations modification may not be reflected in this timestamp. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_pending_transactions_response import GetPendingTransactionsResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89).<br /> It can be omitted if the API key is single-property, or to get results from all properties on an association. (optional)
    include_debit = True # bool | If the response should include debit transactions (optional) (default to True)
    include_credit = True # bool | If the response should include credit transactions (optional) (default to True)
    include_deleted = False # bool | If the response should include deleted transactions (optional) (default to False)
    include_children = False # bool | If the response should include children transactions (requires the parameter transactionIDs) (optional) (default to False)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier, used to filter transactions result If reservationID is informed, and dates are not, all transactions with the reservationID will be returned. (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation Identifier, used to filter transactions result (optional)
    room_id = 'room_id_example' # str | Room ID, used to filter transactions result (optional)
    guest_id = 'guest_id_example' # str | Guest ID, used to filter transactions result (optional)
    house_account_id = 'house_account_id_example' # str | House Account ID, used to filter transactions result (optional)
    transaction_ids = 'transaction_ids_example' # str | List of transaction IDs to be returned, comma-separated, i.e. 37,345,89. (optional)
    results_from = '2013-10-20' # date | Inferior limit date, used to filter transactions result (posted transaction date) (optional)
    results_to = '2013-10-20' # date | Superior limit date, used to filter transactions result (posted transaction date) (optional)
    modified_from = '2013-10-20' # date | Inferior limit date, used to filter transactions result (optional)
    modified_to = '2013-10-20' # date | Superior limit date, used to filter transactions result (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter transactions result (creation date of the transaction). If informed, all other dates are ignored (except createdTo). If createdFrom is informed, but createdTo is not, the call will return all results since this datetime. Necessary only if createdTo is sent. If time portion not given, assumes 00:00:00. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter transactions result (creation date of the transaction). If informed (together with createdFrom), all other dates are ignored. If time portion not given, assumes 23:59:59. (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Sort response results by field (optional)
    order_by = desc # str | Order response in DESCending or ASCending order, used together with sortBy (optional) (default to desc)

    try:
        # getPendingTransactions
        api_response = api_instance.get_pending_transactions_get(property_id=property_id, include_debit=include_debit, include_credit=include_credit, include_deleted=include_deleted, include_children=include_children, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id, guest_id=guest_id, house_account_id=house_account_id, transaction_ids=transaction_ids, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, created_from=created_from, created_to=created_to, page_number=page_number, page_size=page_size, sort_by=sort_by, order_by=order_by)
        print("The response of PaymentApi->get_pending_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_pending_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89).&lt;br /&gt; It can be omitted if the API key is single-property, or to get results from all properties on an association. | [optional] 
 **include_debit** | **bool**| If the response should include debit transactions | [optional] [default to True]
 **include_credit** | **bool**| If the response should include credit transactions | [optional] [default to True]
 **include_deleted** | **bool**| If the response should include deleted transactions | [optional] [default to False]
 **include_children** | **bool**| If the response should include children transactions (requires the parameter transactionIDs) | [optional] [default to False]
 **reservation_id** | **str**| Reservation Unique Identifier, used to filter transactions result If reservationID is informed, and dates are not, all transactions with the reservationID will be returned. | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation Identifier, used to filter transactions result | [optional] 
 **room_id** | **str**| Room ID, used to filter transactions result | [optional] 
 **guest_id** | **str**| Guest ID, used to filter transactions result | [optional] 
 **house_account_id** | **str**| House Account ID, used to filter transactions result | [optional] 
 **transaction_ids** | **str**| List of transaction IDs to be returned, comma-separated, i.e. 37,345,89. | [optional] 
 **results_from** | **date**| Inferior limit date, used to filter transactions result (posted transaction date) | [optional] 
 **results_to** | **date**| Superior limit date, used to filter transactions result (posted transaction date) | [optional] 
 **modified_from** | **date**| Inferior limit date, used to filter transactions result | [optional] 
 **modified_to** | **date**| Superior limit date, used to filter transactions result | [optional] 
 **created_from** | **datetime**| Inferior limit datetime, used to filter transactions result (creation date of the transaction). If informed, all other dates are ignored (except createdTo). If createdFrom is informed, but createdTo is not, the call will return all results since this datetime. Necessary only if createdTo is sent. If time portion not given, assumes 00:00:00. | [optional] 
 **created_to** | **datetime**| Superior limit datetime, used to filter transactions result (creation date of the transaction). If informed (together with createdFrom), all other dates are ignored. If time portion not given, assumes 23:59:59. | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]
 **sort_by** | **str**| Sort response results by field | [optional] 
 **order_by** | **str**| Order response in DESCending or ASCending order, used together with sortBy | [optional] [default to desc]

### Return type

[**GetPendingTransactionsResponse**](GetPendingTransactionsResponse.md)

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

# **get_transactions_get**
> GetTransactionsResponse get_transactions_get(property_id=property_id, include_debit=include_debit, include_credit=include_credit, include_deleted=include_deleted, include_children=include_children, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id, guest_id=guest_id, house_account_id=house_account_id, transaction_ids=transaction_ids, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, service_date_from=service_date_from, service_date_to=service_date_to, created_from=created_from, created_to=created_to, transaction_filter=transaction_filter, page_number=page_number, page_size=page_size, sort_by=sort_by, order_by=order_by)

getTransactions

Get a list of transactions for a property, or list of properties, for the date range specified. If no date range or reservation is specified, it will return the transactions for the last 7 days, unless stated otherwise.<br /> Please note that some reservations modification may not be reflected in this timestamp. ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_transactions_response import GetTransactionsResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | ID for the properties to be queried (comma-separated, i.e. 37,345,89).<br /> It can be omitted if the API key is single-property, or to get results from all properties on an association. (optional)
    include_debit = True # bool | If the response should include debit transactions (optional) (default to True)
    include_credit = True # bool | If the response should include credit transactions (optional) (default to True)
    include_deleted = False # bool | If the response should include deleted transactions (optional) (default to False)
    include_children = False # bool | If the response should include children transactions (requires the parameter transactionIDs) (optional) (default to False)
    reservation_id = 'reservation_id_example' # str | Reservation Unique Identifier, used to filter transactions result If reservationID is informed, and dates are not, all transactions with the reservationID will be returned. (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | Sub Reservation Identifier, used to filter transactions result (optional)
    room_id = 'room_id_example' # str | Room ID, used to filter transactions result (optional)
    guest_id = 'guest_id_example' # str | Guest ID, used to filter transactions result (optional)
    house_account_id = 'house_account_id_example' # str | House Account ID, used to filter transactions result (optional)
    transaction_ids = 'transaction_ids_example' # str | List of transaction IDs to be returned, comma-separated, i.e. 37,345,89. (optional)
    results_from = '2013-10-20' # date | Inferior limit date, used to filter transactions result (posted transaction date) (optional)
    results_to = '2013-10-20' # date | Superior limit date, used to filter transactions result (posted transaction date) (optional)
    modified_from = '2013-10-20' # date | Inferior limit date, used to filter transactions result (optional)
    modified_to = '2013-10-20' # date | Superior limit date, used to filter transactions result (optional)
    service_date_from = '2013-10-20' # date | Filter by the date of the service, the date that was intended the transaction to occured (optional)
    service_date_to = '2013-10-20' # date | Filter by the date of the service, the date that was intended the transaction to occured (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Inferior limit datetime, used to filter transactions result (creation date of the transaction). If informed, all other dates are ignored (except createdTo). If createdFrom is informed, but createdTo is not, the call will return all results since this datetime. Necessary only if createdTo is sent. If time portion not given, assumes 00:00:00. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Superior limit datetime, used to filter transactions result (creation date of the transaction). If informed (together with createdFrom), all other dates are ignored. If time portion not given, assumes 23:59:59. (optional)
    transaction_filter = 'simple_transactions,adjustments,adjustments_voids,voids,refunds' # str | Transaction filter is used to filter transactions result (optional) (default to 'simple_transactions,adjustments,adjustments_voids,voids,refunds')
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Sort response results by field (optional)
    order_by = desc # str | Order response in DESCending or ASCending order, used together with sortBy (optional) (default to desc)

    try:
        # getTransactions
        api_response = api_instance.get_transactions_get(property_id=property_id, include_debit=include_debit, include_credit=include_credit, include_deleted=include_deleted, include_children=include_children, reservation_id=reservation_id, sub_reservation_id=sub_reservation_id, room_id=room_id, guest_id=guest_id, house_account_id=house_account_id, transaction_ids=transaction_ids, results_from=results_from, results_to=results_to, modified_from=modified_from, modified_to=modified_to, service_date_from=service_date_from, service_date_to=service_date_to, created_from=created_from, created_to=created_to, transaction_filter=transaction_filter, page_number=page_number, page_size=page_size, sort_by=sort_by, order_by=order_by)
        print("The response of PaymentApi->get_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| ID for the properties to be queried (comma-separated, i.e. 37,345,89).&lt;br /&gt; It can be omitted if the API key is single-property, or to get results from all properties on an association. | [optional] 
 **include_debit** | **bool**| If the response should include debit transactions | [optional] [default to True]
 **include_credit** | **bool**| If the response should include credit transactions | [optional] [default to True]
 **include_deleted** | **bool**| If the response should include deleted transactions | [optional] [default to False]
 **include_children** | **bool**| If the response should include children transactions (requires the parameter transactionIDs) | [optional] [default to False]
 **reservation_id** | **str**| Reservation Unique Identifier, used to filter transactions result If reservationID is informed, and dates are not, all transactions with the reservationID will be returned. | [optional] 
 **sub_reservation_id** | **str**| Sub Reservation Identifier, used to filter transactions result | [optional] 
 **room_id** | **str**| Room ID, used to filter transactions result | [optional] 
 **guest_id** | **str**| Guest ID, used to filter transactions result | [optional] 
 **house_account_id** | **str**| House Account ID, used to filter transactions result | [optional] 
 **transaction_ids** | **str**| List of transaction IDs to be returned, comma-separated, i.e. 37,345,89. | [optional] 
 **results_from** | **date**| Inferior limit date, used to filter transactions result (posted transaction date) | [optional] 
 **results_to** | **date**| Superior limit date, used to filter transactions result (posted transaction date) | [optional] 
 **modified_from** | **date**| Inferior limit date, used to filter transactions result | [optional] 
 **modified_to** | **date**| Superior limit date, used to filter transactions result | [optional] 
 **service_date_from** | **date**| Filter by the date of the service, the date that was intended the transaction to occured | [optional] 
 **service_date_to** | **date**| Filter by the date of the service, the date that was intended the transaction to occured | [optional] 
 **created_from** | **datetime**| Inferior limit datetime, used to filter transactions result (creation date of the transaction). If informed, all other dates are ignored (except createdTo). If createdFrom is informed, but createdTo is not, the call will return all results since this datetime. Necessary only if createdTo is sent. If time portion not given, assumes 00:00:00. | [optional] 
 **created_to** | **datetime**| Superior limit datetime, used to filter transactions result (creation date of the transaction). If informed (together with createdFrom), all other dates are ignored. If time portion not given, assumes 23:59:59. | [optional] 
 **transaction_filter** | **str**| Transaction filter is used to filter transactions result | [optional] [default to &#39;simple_transactions,adjustments,adjustments_voids,voids,refunds&#39;]
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]
 **sort_by** | **str**| Sort response results by field | [optional] 
 **order_by** | **str**| Order response in DESCending or ASCending order, used together with sortBy | [optional] [default to desc]

### Return type

[**GetTransactionsResponse**](GetTransactionsResponse.md)

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

# **post_charge_post**
> PostChargeResponse post_charge_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_id=group_id, accounts_receivable_ledger_id=accounts_receivable_ledger_id, amount=amount, currency=currency, description=description, payment_method_id=payment_method_id, is_deposit=is_deposit, redirect_url=redirect_url)

postCharge

Use a payment method to process a payment on a reservation, group profile, accounts receivable ledger, or house account.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_charge_response import PostChargeResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str |  (optional)
    reservation_id = 'reservation_id_example' # str | Reservation ID (optional)
    house_account_id = 'house_account_id_example' # str | House Account ID (optional)
    group_id = 'group_id_example' # str | Group ID (optional)
    accounts_receivable_ledger_id = 'accounts_receivable_ledger_id_example' # str | Accounts Receivable Ledger ID (optional)
    amount = 'amount_example' # str | Amount to charge (optional)
    currency = 'currency_example' # str | Currency to charge (optional)
    description = 'description_example' # str | Description of the payment to display on folio (optional)
    payment_method_id = 'payment_method_id_example' # str | Payment method UUID (optional)
    is_deposit = True # bool | determine if this payment is a deposit (default: false) (optional)
    redirect_url = 'redirect_url_example' # str | client will be redirected to this page after he completed 3ds challenge. User will be redirected with HTTP get redirect and parameter **result** will be added to query string with possible values: - **failed** if 3ds challenge is not passed - **successful** if 3ds challenge is passed If not provided for card with 3ds the request will be rejected (optional)

    try:
        # postCharge
        api_response = api_instance.post_charge_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_id=group_id, accounts_receivable_ledger_id=accounts_receivable_ledger_id, amount=amount, currency=currency, description=description, payment_method_id=payment_method_id, is_deposit=is_deposit, redirect_url=redirect_url)
        print("The response of PaymentApi->post_charge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_charge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  | [optional] 
 **reservation_id** | **str**| Reservation ID | [optional] 
 **house_account_id** | **str**| House Account ID | [optional] 
 **group_id** | **str**| Group ID | [optional] 
 **accounts_receivable_ledger_id** | **str**| Accounts Receivable Ledger ID | [optional] 
 **amount** | **str**| Amount to charge | [optional] 
 **currency** | **str**| Currency to charge | [optional] 
 **description** | **str**| Description of the payment to display on folio | [optional] 
 **payment_method_id** | **str**| Payment method UUID | [optional] 
 **is_deposit** | **bool**| determine if this payment is a deposit (default: false) | [optional] 
 **redirect_url** | **str**| client will be redirected to this page after he completed 3ds challenge. User will be redirected with HTTP get redirect and parameter **result** will be added to query string with possible values: - **failed** if 3ds challenge is not passed - **successful** if 3ds challenge is passed If not provided for card with 3ds the request will be rejected | [optional] 

### Return type

[**PostChargeResponse**](PostChargeResponse.md)

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

# **post_credit_card_post**
> PostCardResponse post_credit_card_post(property_id=property_id, reservation_id=reservation_id, card_token=card_token, payment_method_id=payment_method_id, return_url=return_url)

postCreditCard

Returns the rate of the room type selected, based on the provided parameters

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_card_response import PostCardResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str |  (optional)
    reservation_id = 'reservation_id_example' # str |  (optional)
    card_token = 'card_token_example' # str | cardToken provided by Stripe JS, not recommended, not required if paymentMethodId is provided (optional)
    payment_method_id = 'payment_method_id_example' # str | Payment Method ID provided by the payments SDK (optional)
    return_url = 'return_url_example' # str | client will be redirected to this page after he completed 3ds challenge. User will be redirected with HTTP get redirect and parameter **result** will be added to query string with possible values: - **failed** if 3ds challenge is not passed - **successful** if 3ds challenge is passed If not provided for card with 3ds the request will be rejected (optional)

    try:
        # postCreditCard
        api_response = api_instance.post_credit_card_post(property_id=property_id, reservation_id=reservation_id, card_token=card_token, payment_method_id=payment_method_id, return_url=return_url)
        print("The response of PaymentApi->post_credit_card_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_credit_card_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**|  | [optional] 
 **reservation_id** | **str**|  | [optional] 
 **card_token** | **str**| cardToken provided by Stripe JS, not recommended, not required if paymentMethodId is provided | [optional] 
 **payment_method_id** | **str**| Payment Method ID provided by the payments SDK | [optional] 
 **return_url** | **str**| client will be redirected to this page after he completed 3ds challenge. User will be redirected with HTTP get redirect and parameter **result** will be added to query string with possible values: - **failed** if 3ds challenge is not passed - **successful** if 3ds challenge is passed If not provided for card with 3ds the request will be rejected | [optional] 

### Return type

[**PostCardResponse**](PostCardResponse.md)

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

# **post_custom_payment_method_post**
> PostCustomPaymentMethodResponse post_custom_payment_method_post(property_id=property_id, method=method, method_name=method_name)

postCustomPaymentMethod

Add a Custom Payment Method to a property. This call does not allow to add Payment Methods: credit cards, bank transfer or Pay Pal.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_custom_payment_method_response import PostCustomPaymentMethodResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | Property ID, if not sent will retrieve property ID from credentials, only one property ID call. (optional)
    method = 'method_example' # str | Payment Method, value used in future calls. Must be unique for each property and no whitespaces are allowed (use camel case or underline instead). Will be verified against existing Payment Methods, if it exists, will try to enable it. (optional)
    method_name = 'method_name_example' # str | Payment Method Name, value used to represent the Payment Method. Can use spaces. If nothing is sent, will use value for method. (optional)

    try:
        # postCustomPaymentMethod
        api_response = api_instance.post_custom_payment_method_post(property_id=property_id, method=method, method_name=method_name)
        print("The response of PaymentApi->post_custom_payment_method_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_custom_payment_method_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID, if not sent will retrieve property ID from credentials, only one property ID call. | [optional] 
 **method** | **str**| Payment Method, value used in future calls. Must be unique for each property and no whitespaces are allowed (use camel case or underline instead). Will be verified against existing Payment Methods, if it exists, will try to enable it. | [optional] 
 **method_name** | **str**| Payment Method Name, value used to represent the Payment Method. Can use spaces. If nothing is sent, will use value for method. | [optional] 

### Return type

[**PostCustomPaymentMethodResponse**](PostCustomPaymentMethodResponse.md)

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

# **post_payment_cash_post**
> PostPaymentCashResponse post_payment_cash_post(reservation_id=reservation_id, amount=amount)

postPaymentCash

Add a payment done by cash to a specified reservation

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_payment_cash_response import PostPaymentCashResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    amount = 3.4 # float | Amount paid on this payment (optional)

    try:
        # postPaymentCash
        api_response = api_instance.post_payment_cash_post(reservation_id=reservation_id, amount=amount)
        print("The response of PaymentApi->post_payment_cash_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_payment_cash_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **amount** | **float**| Amount paid on this payment | [optional] 

### Return type

[**PostPaymentCashResponse**](PostPaymentCashResponse.md)

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

# **post_payment_credit_card_post**
> PostPaymentCreditCardResponse post_payment_credit_card_post(reservation_id=reservation_id, amount=amount, card_id=card_id)

postPaymentCreditCard

Add a payment done by credit card to a specified reservation

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_payment_credit_card_response import PostPaymentCreditCardResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    amount = 3.4 # float | Amount paid on this payment (optional)
    card_id = 'card_id_example' # str | Credit Card ID used on payment. Can be retrieved with reservation information (optional)

    try:
        # postPaymentCreditCard
        api_response = api_instance.post_payment_credit_card_post(reservation_id=reservation_id, amount=amount, card_id=card_id)
        print("The response of PaymentApi->post_payment_credit_card_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_payment_credit_card_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **amount** | **float**| Amount paid on this payment | [optional] 
 **card_id** | **str**| Credit Card ID used on payment. Can be retrieved with reservation information | [optional] 

### Return type

[**PostPaymentCreditCardResponse**](PostPaymentCreditCardResponse.md)

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

# **post_payment_post**
> PostPaymentResponse post_payment_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, sub_reservation_id=sub_reservation_id, type=type, amount=amount, card_type=card_type, description=description, is_deposit=is_deposit)

postPayment

Add a payment to a specified reservation or house account. If both Reservation ID and HouseAccountID are informed, only the former is taken in consideration.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_payment_response import PostPaymentResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    house_account_id = 'house_account_id_example' # str | House Account identifier is necessary if reservationID not sent (optional)
    sub_reservation_id = 'sub_reservation_id_example' # str | The Sub Reservation identifier. reservationID is still mandatory if subReservationID is sent. (optional)
    type = 'type_example' # str | Payment type. Use the call [getPaymentMethods](#api-Payment-getPaymentMethods) to get the properties enabled payment methods. (optional)
    amount = 3.4 # float | Amount paid on this transaction (optional)
    card_type = 'card_type_example' # str | If type = credit, cardType is necessary. Allowed values are property based, but possible strings are: \\\"visa\\\",\\\"master\\\",\\\"amex\\\",\\\"aura\\\",\\\"diners\\\",\\\"hiper\\\",\\\"elo\\\",\\\"Discover\\\",\\\"jcb\\\",\\\"maestro\\\",\\\"dan\\\",\\\"PostCard\\\",\\\"Eurocard\\\",\\\"union_pay\\\" (optional)
    description = 'description_example' # str | Note to be added to payment (optional)
    is_deposit = True # bool | determine if this payment is a deposit (default: false) (optional)

    try:
        # postPayment
        api_response = api_instance.post_payment_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, sub_reservation_id=sub_reservation_id, type=type, amount=amount, card_type=card_type, description=description, is_deposit=is_deposit)
        print("The response of PaymentApi->post_payment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_payment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **house_account_id** | **str**| House Account identifier is necessary if reservationID not sent | [optional] 
 **sub_reservation_id** | **str**| The Sub Reservation identifier. reservationID is still mandatory if subReservationID is sent. | [optional] 
 **type** | **str**| Payment type. Use the call [getPaymentMethods](#api-Payment-getPaymentMethods) to get the properties enabled payment methods. | [optional] 
 **amount** | **float**| Amount paid on this transaction | [optional] 
 **card_type** | **str**| If type &#x3D; credit, cardType is necessary. Allowed values are property based, but possible strings are: \\\&quot;visa\\\&quot;,\\\&quot;master\\\&quot;,\\\&quot;amex\\\&quot;,\\\&quot;aura\\\&quot;,\\\&quot;diners\\\&quot;,\\\&quot;hiper\\\&quot;,\\\&quot;elo\\\&quot;,\\\&quot;Discover\\\&quot;,\\\&quot;jcb\\\&quot;,\\\&quot;maestro\\\&quot;,\\\&quot;dan\\\&quot;,\\\&quot;PostCard\\\&quot;,\\\&quot;Eurocard\\\&quot;,\\\&quot;union_pay\\\&quot; | [optional] 
 **description** | **str**| Note to be added to payment | [optional] 
 **is_deposit** | **bool**| determine if this payment is a deposit (default: false) | [optional] 

### Return type

[**PostPaymentResponse**](PostPaymentResponse.md)

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

# **post_void_payment_post**
> PostVoidPaymentResponse post_void_payment_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, payment_id=payment_id)

postVoidPayment

Voids a payment (using paymentID) to a specified reservation or house account.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_void_payment_response import PostVoidPaymentResponse
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
    api_instance = cloudbeds_pms_v1_3.PaymentApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    house_account_id = 'house_account_id_example' # str | House Account identifier is necessary if reservationID not sent (optional)
    payment_id = 'payment_id_example' # str | paymentID of transaction that should be voided. (optional)

    try:
        # postVoidPayment
        api_response = api_instance.post_void_payment_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, payment_id=payment_id)
        print("The response of PaymentApi->post_void_payment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->post_void_payment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **house_account_id** | **str**| House Account identifier is necessary if reservationID not sent | [optional] 
 **payment_id** | **str**| paymentID of transaction that should be voided. | [optional] 

### Return type

[**PostVoidPaymentResponse**](PostVoidPaymentResponse.md)

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

