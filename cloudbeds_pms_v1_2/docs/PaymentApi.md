# cloudbeds_pms_v1_2.PaymentApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_methods_get**](PaymentApi.md#get_payment_methods_get) | **GET** /getPaymentMethods | getPaymentMethods
[**get_payments_capabilities_get**](PaymentApi.md#get_payments_capabilities_get) | **GET** /getPaymentsCapabilities | getPaymentsCapabilities
[**post_charge_post**](PaymentApi.md#post_charge_post) | **POST** /postCharge | postCharge
[**post_credit_card_post**](PaymentApi.md#post_credit_card_post) | **POST** /postCreditCard | postCreditCard
[**post_custom_payment_method_post**](PaymentApi.md#post_custom_payment_method_post) | **POST** /postCustomPaymentMethod | postCustomPaymentMethod
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
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_payment_methods_response import GetPaymentMethodsResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_payments_capabilities_response import GetPaymentsCapabilitiesResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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

# **post_charge_post**
> PostChargeResponse post_charge_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, group_id=group_id, accounts_receivable_ledger_id=accounts_receivable_ledger_id, amount=amount, currency=currency, description=description, payment_method_id=payment_method_id, is_deposit=is_deposit, redirect_url=redirect_url)

postCharge

Use a payment method to process a payment on a reservation, group profile, accounts receivable ledger, or house account.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_charge_response import PostChargeResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_card_response import PostCardResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_custom_payment_method_response import PostCustomPaymentMethodResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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

# **post_payment_post**
> PostPaymentResponse post_payment_post(property_id=property_id, reservation_id=reservation_id, house_account_id=house_account_id, sub_reservation_id=sub_reservation_id, type=type, amount=amount, card_type=card_type, description=description, is_deposit=is_deposit)

postPayment

Add a payment to a specified reservation or house account. If both Reservation ID and HouseAccountID are informed, only the former is taken in consideration.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_payment_response import PostPaymentResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_void_payment_response import PostVoidPaymentResponse
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
    api_instance = cloudbeds_pms_v1_2.PaymentApi(api_client)
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

