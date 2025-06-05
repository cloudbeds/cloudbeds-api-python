# cloudbeds_pms_v1_3.AdjustmentApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_adjustment_delete**](AdjustmentApi.md#delete_adjustment_delete) | **DELETE** /deleteAdjustment | deleteAdjustment
[**post_adjustment_post**](AdjustmentApi.md#post_adjustment_post) | **POST** /postAdjustment | postAdjustment


# **delete_adjustment_delete**
> DeleteAdjustmentResponse delete_adjustment_delete(reservation_id, adjustment_id, property_id=property_id)

deleteAdjustment

Voids the AdjustmentID transaction on the specified reservationID

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.delete_adjustment_response import DeleteAdjustmentResponse
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
    api_instance = cloudbeds_pms_v1_3.AdjustmentApi(api_client)
    reservation_id = 'reservation_id_example' # str | Reservation identifier
    adjustment_id = 'adjustment_id_example' # str | Adjustment identifier
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # deleteAdjustment
        api_response = api_instance.delete_adjustment_delete(reservation_id, adjustment_id, property_id=property_id)
        print("The response of AdjustmentApi->delete_adjustment_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentApi->delete_adjustment_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| Reservation identifier | 
 **adjustment_id** | **str**| Adjustment identifier | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**DeleteAdjustmentResponse**](DeleteAdjustmentResponse.md)

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

# **post_adjustment_post**
> PostAdjustmentResponse post_adjustment_post(property_id=property_id, reservation_id=reservation_id, type=type, amount=amount, notes=notes, item_id=item_id)

postAdjustment

Adds an adjustment to a reservation

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_adjustment_response import PostAdjustmentResponse
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
    api_instance = cloudbeds_pms_v1_3.AdjustmentApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    reservation_id = 'reservation_id_example' # str | Reservation identifier (optional)
    type = 'type_example' # str | Apply Adjustment to (optional)
    amount = 3.4 # float | Adjustment amount (optional)
    notes = 'notes_example' # str | Adjustment notes (optional)
    item_id = 'item_id_example' # str | Apply Adjustment to. Identifier for: product, tax, fee. Not for rate (optional)

    try:
        # postAdjustment
        api_response = api_instance.post_adjustment_post(property_id=property_id, reservation_id=reservation_id, type=type, amount=amount, notes=notes, item_id=item_id)
        print("The response of AdjustmentApi->post_adjustment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentApi->post_adjustment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **reservation_id** | **str**| Reservation identifier | [optional] 
 **type** | **str**| Apply Adjustment to | [optional] 
 **amount** | **float**| Adjustment amount | [optional] 
 **notes** | **str**| Adjustment notes | [optional] 
 **item_id** | **str**| Apply Adjustment to. Identifier for: product, tax, fee. Not for rate | [optional] 

### Return type

[**PostAdjustmentResponse**](PostAdjustmentResponse.md)

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

