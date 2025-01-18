# cloudbeds_pms_v1_2.InvoicesApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_get**](InvoicesApi.md#get_invoice_get) | **GET** /getInvoice | getInvoice
[**patch_invoice_post**](InvoicesApi.md#patch_invoice_post) | **POST** /patchInvoice | patchInvoice


# **get_invoice_get**
> GetInvoiceResponse get_invoice_get(invoice_id, property_id=property_id)

getInvoice

Returns invoice data. This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_invoice_response import GetInvoiceResponse
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
    api_instance = cloudbeds_pms_v1_2.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | Invoice ID
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getInvoice
        api_response = api_instance.get_invoice_get(invoice_id, property_id=property_id)
        print("The response of InvoicesApi->get_invoice_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| Invoice ID | 
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

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

# **patch_invoice_post**
> PostPatchInvoiceResponse patch_invoice_post(property_id=property_id, invoice_id=invoice_id, status=status, file=file)

patchInvoice

Update invoice state. This call is only available for third-party integration partners, and not for property client IDs.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_patch_invoice_response import PostPatchInvoiceResponse
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
    api_instance = cloudbeds_pms_v1_2.InvoicesApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    invoice_id = 'invoice_id_example' # str | Invoice unique ID (optional)
    status = 'status_example' # str | Desired new invoice status (optional)
    file = None # bytearray | Form-based Credit Notes PDF File.<br/> Allowed file types: <code>*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml</code><br/> Allowed max file size: 10MB<br/> <i>Not required for `failed` status</i> (optional)

    try:
        # patchInvoice
        api_response = api_instance.patch_invoice_post(property_id=property_id, invoice_id=invoice_id, status=status, file=file)
        print("The response of InvoicesApi->patch_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->patch_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **invoice_id** | **str**| Invoice unique ID | [optional] 
 **status** | **str**| Desired new invoice status | [optional] 
 **file** | **bytearray**| Form-based Credit Notes PDF File.&lt;br/&gt; Allowed file types: &lt;code&gt;*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml&lt;/code&gt;&lt;br/&gt; Allowed max file size: 10MB&lt;br/&gt; &lt;i&gt;Not required for &#x60;failed&#x60; status&lt;/i&gt; | [optional] 

### Return type

[**PostPatchInvoiceResponse**](PostPatchInvoiceResponse.md)

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

