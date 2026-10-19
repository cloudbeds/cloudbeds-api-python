# cloudbeds_pms.ChecksApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_controller_create_check**](ChecksApi.md#check_controller_create_check) | **POST** /folio/v1/checks | Post a completed POS check (e.g., F&amp;B) to a guest folio, house account, or group profile
[**check_controller_delete_check**](ChecksApi.md#check_controller_delete_check) | **DELETE** /folio/v1/checks/{checkId} | Void a posted check end-to-end (ledger + payments + its gratuities) by its checkId


# **check_controller_create_check**
> PostCheckResponseSchema check_controller_create_check(x_property_id, idempotency_key, post_check_request_schema)

Post a completed POS check (e.g., F&B) to a guest folio, house account, or group profile

Replaces postCustomItem with first-class folio transactions enriched with hospitality POS context (check identity, revenue center, meal period, gratuity, service charge). Items posted via this endpoint are recorded as regular folio items, not Custom Items, and are tagged as POS-originated for UI differentiation.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.post_check_request_schema import PostCheckRequestSchema
from cloudbeds_pms.models.post_check_response_schema import PostCheckResponseSchema
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
    api_instance = cloudbeds_pms.ChecksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    idempotency_key = 'req-2026-05-05-2047-9b3f' # str | Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400.
    post_check_request_schema = cloudbeds_pms.PostCheckRequestSchema() # PostCheckRequestSchema | Check details: account target, line items, optional gratuities, service charge, discounts and payments.

    try:
        # Post a completed POS check (e.g., F&B) to a guest folio, house account, or group profile
        api_response = api_instance.check_controller_create_check(x_property_id, idempotency_key, post_check_request_schema)
        print("The response of ChecksApi->check_controller_create_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->check_controller_create_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **idempotency_key** | **str**| Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400. | 
 **post_check_request_schema** | [**PostCheckRequestSchema**](PostCheckRequestSchema.md)| Check details: account target, line items, optional gratuities, service charge, discounts and payments. | 

### Return type

[**PostCheckResponseSchema**](PostCheckResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Check successfully posted. The response includes the public checkId (for downstream void/reversal) and the resolved checkNumber. |  -  |
**400** | Bad request — missing/oversized Idempotency-Key header, invalid parameters, validation failures, or unmatched tax/fee IDs. See CheckErrorCodeEnumSchema for the structured error codes returned in the body. |  -  |
**403** | Forbidden — insufficient permissions on the requested property. |  -  |
**404** | Not found — reservation, house account, group, or folio not found. |  -  |
**409** | Conflict — see CheckErrorCodeEnumSchema for the structured codes: IDEMPOTENCY_KEY_REUSED (Idempotency-Key header reused with a different payload), PRODUCT_NAME_CONFLICT (line&#39;s name collides with an existing active product that has a different SKU). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_controller_delete_check**
> object check_controller_delete_check(x_property_id, check_id)

Void a posted check end-to-end (ledger + payments + its gratuities) by its checkId

Voids the whole check: reverses each line (item / service charge / discount) and its tax/fee children on both CDC and DOMAIN, cascade-voids every gratuity linked to the check (each with its own tax children), and voids the anchored payments via the payments service. Idempotent — voiding an already-voided check returns 204.

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
    api_instance = cloudbeds_pms.ChecksApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    check_id = 'check_id_example' # str | The check's public checkId (partner-supplied or Cloudbeds-generated) returned by createCheck.

    try:
        # Void a posted check end-to-end (ledger + payments + its gratuities) by its checkId
        api_response = api_instance.check_controller_delete_check(x_property_id, check_id)
        print("The response of ChecksApi->check_controller_delete_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->check_controller_delete_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **check_id** | **str**| The check&#39;s public checkId (partner-supplied or Cloudbeds-generated) returned by createCheck. | 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Check voided (or already voided — idempotent). |  -  |
**403** | Forbidden — insufficient permissions on the requested property. |  -  |
**404** | Not found — no check matches the checkId on this property (CHECK_NOT_FOUND). |  -  |
**409** | Conflict — the check&#39;s folio target was never persisted (pre-feature posting) (CHECK_VOID_UNAVAILABLE). |  -  |
**500** | Internal server error — ledger void completed but one or more payment voids failed (PAYMENT_VOID_FAILED). Retry to converge. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

