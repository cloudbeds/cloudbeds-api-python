# cloudbeds_pms.GratuitiesApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gratuity_controller_create_check_gratuity**](GratuitiesApi.md#gratuity_controller_create_check_gratuity) | **POST** /folio/v1/checks/{checkId}/gratuities | Post one or more guest tips linked to an existing check
[**gratuity_controller_create_gratuity**](GratuitiesApi.md#gratuity_controller_create_gratuity) | **POST** /folio/v1/gratuities | Post one or more guest tips to a folio, house account, or group profile
[**gratuity_controller_delete_gratuity**](GratuitiesApi.md#gratuity_controller_delete_gratuity) | **DELETE** /folio/v1/gratuities/{gratuityId} | Void a posted gratuity by its gratuityId


# **gratuity_controller_create_check_gratuity**
> PostGratuityResponseSchema gratuity_controller_create_check_gratuity(x_property_id, idempotency_key, check_id, post_check_gratuity_request_schema)

Post one or more guest tips linked to an existing check

Posts one or more tips (ITC 8995) linked to the check identified by the path {checkId}. The gratuities inherit the check's folio target and checkNumber; POS context stays an attribute of the linked check (not copied onto the gratuity). The body carries only the gratuity entries. A check may carry many gratuities. Idempotent via the required Idempotency-Key header.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.post_check_gratuity_request_schema import PostCheckGratuityRequestSchema
from cloudbeds_pms.models.post_gratuity_response_schema import PostGratuityResponseSchema
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
    api_instance = cloudbeds_pms.GratuitiesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    idempotency_key = 'req-2026-05-05-2047-9b3f' # str | Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400.
    check_id = 'check_id_example' # str | The partner checkId of the check to link these gratuities to.
    post_check_gratuity_request_schema = cloudbeds_pms.PostCheckGratuityRequestSchema() # PostCheckGratuityRequestSchema | Gratuity entries to link to the check.

    try:
        # Post one or more guest tips linked to an existing check
        api_response = api_instance.gratuity_controller_create_check_gratuity(x_property_id, idempotency_key, check_id, post_check_gratuity_request_schema)
        print("The response of GratuitiesApi->gratuity_controller_create_check_gratuity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GratuitiesApi->gratuity_controller_create_check_gratuity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **idempotency_key** | **str**| Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400. | 
 **check_id** | **str**| The partner checkId of the check to link these gratuities to. | 
 **post_check_gratuity_request_schema** | [**PostCheckGratuityRequestSchema**](PostCheckGratuityRequestSchema.md)| Gratuity entries to link to the check. | 

### Return type

[**PostGratuityResponseSchema**](PostGratuityResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Gratuity successfully posted. Returns the Cloudbeds-assigned gratuityId for each posted gratuity and notice&#x3D;null. |  -  |
**400** | Bad request — missing/oversized Idempotency-Key header, validation failure, unmatched tax externalId/taxId, unknown recipient userId, or the resolved check carries no folio target. See GratuityErrorCodeEnumSchema. |  -  |
**403** | Forbidden — insufficient permissions on the requested property. |  -  |
**404** | Not found — no check matches {checkId} on this property (CHECK_NOT_FOUND). |  -  |
**409** | Conflict — IDEMPOTENCY_KEY_REUSED (Idempotency-Key reused with a different payload) or DUPLICATE_GRATUITY_ID (a partner-supplied gratuityId collides with an active gratuity). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gratuity_controller_create_gratuity**
> PostGratuityResponseSchema gratuity_controller_create_gratuity(x_property_id, idempotency_key, post_gratuity_request_schema)

Post one or more guest tips to a folio, house account, or group profile

Posts one or more tips (ITC 8995) as first-class folio transactions. Recipient attribution and POS context are stored MFD-side only; the Accounting Service Transaction carries the accounting state alone. Idempotent via the required Idempotency-Key header.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.post_gratuity_request_schema import PostGratuityRequestSchema
from cloudbeds_pms.models.post_gratuity_response_schema import PostGratuityResponseSchema
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
    api_instance = cloudbeds_pms.GratuitiesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    idempotency_key = 'req-2026-05-05-2047-9b3f' # str | Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400.
    post_gratuity_request_schema = cloudbeds_pms.PostGratuityRequestSchema() # PostGratuityRequestSchema | Gratuity posting request: folio target and one or more gratuity entries.

    try:
        # Post one or more guest tips to a folio, house account, or group profile
        api_response = api_instance.gratuity_controller_create_gratuity(x_property_id, idempotency_key, post_gratuity_request_schema)
        print("The response of GratuitiesApi->gratuity_controller_create_gratuity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GratuitiesApi->gratuity_controller_create_gratuity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **idempotency_key** | **str**| Required per-request idempotency key and the sole dedup key for this endpoint: a retry carrying the same key and the same payload replays the original posting (notice populated); the same key with a different payload is rejected with IDEMPOTENCY_KEY_REUSED. Absent, empty, or whitespace-only → 400. | 
 **post_gratuity_request_schema** | [**PostGratuityRequestSchema**](PostGratuityRequestSchema.md)| Gratuity posting request: folio target and one or more gratuity entries. | 

### Return type

[**PostGratuityResponseSchema**](PostGratuityResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Gratuity successfully posted. Returns the Cloudbeds-assigned gratuityId for each posted gratuity and notice&#x3D;null. |  -  |
**400** | Bad request — missing/oversized Idempotency-Key header, validation failure, unmatched tax externalId/taxId, unknown recipient userId, or an unresolvable folio target. See GratuityErrorCodeEnumSchema for structured error codes. |  -  |
**403** | Forbidden — insufficient permissions on the requested property. |  -  |
**409** | Conflict — see GratuityErrorCodeEnumSchema for the structured codes: IDEMPOTENCY_KEY_REUSED (Idempotency-Key reused with a different payload) or DUPLICATE_GRATUITY_ID (a partner-supplied gratuityId collides with an active gratuity). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gratuity_controller_delete_gratuity**
> object gratuity_controller_delete_gratuity(x_property_id, gratuity_id)

Void a posted gratuity by its gratuityId

Voids a single gratuity (as returned at post time) — reverses its tip line and its tax children on both CDC and DOMAIN. Idempotent: voiding an already-voided gratuity returns 204. The gratuityId is not re-issued after void.

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
    api_instance = cloudbeds_pms.GratuitiesApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    gratuity_id = 'gratuity_id_example' # str | The public gratuityId of the gratuity to void, as returned at post time.

    try:
        # Void a posted gratuity by its gratuityId
        api_response = api_instance.gratuity_controller_delete_gratuity(x_property_id, gratuity_id)
        print("The response of GratuitiesApi->gratuity_controller_delete_gratuity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GratuitiesApi->gratuity_controller_delete_gratuity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **gratuity_id** | **str**| The public gratuityId of the gratuity to void, as returned at post time. | 

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
**204** | Gratuity voided (or already voided — idempotent). |  -  |
**403** | Forbidden — insufficient permissions on the requested property. |  -  |
**404** | Not found — no gratuity matches the gratuityId on this property (GRATUITY_NOT_FOUND). |  -  |
**409** | Conflict — the gratuity predates void support and cannot be voided (GRATUITY_VOID_UNAVAILABLE). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

