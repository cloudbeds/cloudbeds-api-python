# cloudbeds_pms.PaymentsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /payments/v1/payments | Create a payment or authorization


# **create_payment**
> CreatePaymentResponseSchema create_payment(x_property_id, create_payment_request_schema)

Create a payment or authorization

Creates a payment with the specified capture mode. Use 'auto' for immediate charge, 'manual' for authorization only.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.create_payment_request_schema import CreatePaymentRequestSchema
from cloudbeds_pms.models.create_payment_response_schema import CreatePaymentResponseSchema
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
    api_instance = cloudbeds_pms.PaymentsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    create_payment_request_schema = cloudbeds_pms.CreatePaymentRequestSchema() # CreatePaymentRequestSchema | Payment creation request

    try:
        # Create a payment or authorization
        api_response = api_instance.create_payment(x_property_id, create_payment_request_schema)
        print("The response of PaymentsApi->create_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **create_payment_request_schema** | [**CreatePaymentRequestSchema**](CreatePaymentRequestSchema.md)| Payment creation request | 

### Return type

[**CreatePaymentResponseSchema**](CreatePaymentResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Payment created successfully |  -  |
**400** | Bad request - invalid parameters or validation errors |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Not found - inventory object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

