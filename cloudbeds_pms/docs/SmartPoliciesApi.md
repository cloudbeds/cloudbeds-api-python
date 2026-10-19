# cloudbeds_pms.SmartPoliciesApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjustment_preview_controller_preview**](SmartPoliciesApi.md#adjustment_preview_controller_preview) | **POST** /smart-policies/v1/payments/preview-adjustment | Preview how a folio adjustment (tax/fee/rate/room-revenue) would affect Smart Policy scheduled payments.
[**get_booking_policy_information_controller_get_booking_policy_information**](SmartPoliciesApi.md#get_booking_policy_information_controller_get_booking_policy_information) | **GET** /smart-policies/v1/reservations/{reservationId}/policy-information | Get the rendered smart policy text and scheduled payments for a reservation.


# **adjustment_preview_controller_preview**
> PreviewAdjustmentResponseSchema adjustment_preview_controller_preview(x_property_id, preview_adjustment_request_schema)

Preview how a folio adjustment (tax/fee/rate/room-revenue) would affect Smart Policy scheduled payments.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.preview_adjustment_request_schema import PreviewAdjustmentRequestSchema
from cloudbeds_pms.models.preview_adjustment_response_schema import PreviewAdjustmentResponseSchema
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
    api_instance = cloudbeds_pms.SmartPoliciesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    preview_adjustment_request_schema = cloudbeds_pms.PreviewAdjustmentRequestSchema() # PreviewAdjustmentRequestSchema | Adjustment preview input.

    try:
        # Preview how a folio adjustment (tax/fee/rate/room-revenue) would affect Smart Policy scheduled payments.
        api_response = api_instance.adjustment_preview_controller_preview(x_property_id, preview_adjustment_request_schema)
        print("The response of SmartPoliciesApi->adjustment_preview_controller_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPoliciesApi->adjustment_preview_controller_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **preview_adjustment_request_schema** | [**PreviewAdjustmentRequestSchema**](PreviewAdjustmentRequestSchema.md)| Adjustment preview input. | 

### Return type

[**PreviewAdjustmentResponseSchema**](PreviewAdjustmentResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adjustment preview result. |  -  |
**400** | Bad request response. |  -  |
**403** | Forbidden response. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_booking_policy_information_controller_get_booking_policy_information**
> BookingPolicyInformationResponseSchema get_booking_policy_information_controller_get_booking_policy_information(x_property_id, reservation_id, language_code=language_code)

Get the rendered smart policy text and scheduled payments for a reservation.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.booking_policy_information_response_schema import BookingPolicyInformationResponseSchema
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
    api_instance = cloudbeds_pms.SmartPoliciesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    reservation_id = cloudbeds_pms.ReservationId() # ReservationId | Reservation identifier.
    language_code = 'language_code_example' # str | Language code for the rendered policy text (e.g. \"fr\", \"en-US\"). Defaults to the property's language when omitted. (optional)

    try:
        # Get the rendered smart policy text and scheduled payments for a reservation.
        api_response = api_instance.get_booking_policy_information_controller_get_booking_policy_information(x_property_id, reservation_id, language_code=language_code)
        print("The response of SmartPoliciesApi->get_booking_policy_information_controller_get_booking_policy_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartPoliciesApi->get_booking_policy_information_controller_get_booking_policy_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **reservation_id** | **ReservationId**| Reservation identifier. | 
 **language_code** | **str**| Language code for the rendered policy text (e.g. \&quot;fr\&quot;, \&quot;en-US\&quot;). Defaults to the property&#39;s language when omitted. | [optional] 

### Return type

[**BookingPolicyInformationResponseSchema**](BookingPolicyInformationResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy information for the reservation. When the reservation is not governed by a smart policy, falls back to the property&#39;s legacy cancellation policy text (policyTextSource&#x3D;\&quot;legacy\&quot;); when neither is available, returns a null policyText rather than an error. |  -  |
**400** | Bad request response. |  -  |
**403** | The API client is not authorized for this property or lacks the required scope. |  -  |
**404** | No reservation with the given identifier exists for the requesting property. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

