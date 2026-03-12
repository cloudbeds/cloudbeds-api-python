# cloudbeds_pms_v1_3.CustomFieldsApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_fields_get**](CustomFieldsApi.md#get_custom_fields_get) | **GET** /getCustomFields | getCustomFields
[**post_custom_field_post**](CustomFieldsApi.md#post_custom_field_post) | **POST** /postCustomField | postCustomField


# **get_custom_fields_get**
> GetCustomFieldsResponse get_custom_fields_get(property_id=property_id, custom_field_id=custom_field_id, shortcode=shortcode)

getCustomFields

Gets custom fields list<br /> ¹ data.displayed = "booking" - Display this field to guests on the booking engine.<br /> ¹ data.displayed = "reservation" - Add this field to the reservation folio for use by staff.<br /> ¹ data.displayed = "card" - Make this field available for registration cards.<br />

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_custom_fields_response import GetCustomFieldsResponse
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
    api_instance = cloudbeds_pms_v1_3.CustomFieldsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    custom_field_id = 'custom_field_id_example' # str | Field identifier (optional)
    shortcode = 'shortcode_example' # str | Internal reference and is used for integration purposes such as custom links and the API (optional)

    try:
        # getCustomFields
        api_response = api_instance.get_custom_fields_get(property_id=property_id, custom_field_id=custom_field_id, shortcode=shortcode)
        print("The response of CustomFieldsApi->get_custom_fields_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_fields_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **custom_field_id** | **str**| Field identifier | [optional] 
 **shortcode** | **str**| Internal reference and is used for integration purposes such as custom links and the API | [optional] 

### Return type

[**GetCustomFieldsResponse**](GetCustomFieldsResponse.md)

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

# **post_custom_field_post**
> PostCustomFieldResponse post_custom_field_post(property_id=property_id, name=name, shortcode=shortcode, apply_to=apply_to, required=required, max_characters=max_characters, type=type, displayed=displayed, is_personal=is_personal)

postCustomField

Sets custom fields. The call should only be made once to add the field to the system.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_custom_field_response import PostCustomFieldResponse
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
    api_instance = cloudbeds_pms_v1_3.CustomFieldsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    name = 'name_example' # str | Field name (optional)
    shortcode = 'shortcode_example' # str | Internal reference and is used for integration purposes such as custom links and the API (optional)
    apply_to = reservation # str | Where put this field in reservation or guest section of the booking. reservation - applies the custom field to reservations in myfrontdesk guest - applies the custom field to guest interface in myfrontdesk (optional) (default to reservation)
    required = False # bool | Specify whether this field is required to be filled out. (optional) (default to False)
    max_characters = 40 # int | Maximum number of characters allowed to be entered in this field. (optional) (default to 40)
    type = input # str | The field's input type. (optional) (default to input)
    displayed = ['displayed_example'] # List[str] | ¹ Specify where this custom field to show up. reservation - applies the custom field to reservation interface in myfrontdesk booking - applies the custom field to the booking engine card - applies the custom field to Registration cards (optional)
    is_personal = True # bool | Specifies if the contents of this field may contain personal information. User's personal information may be removed upon request according to GDPR rules. (optional)

    try:
        # postCustomField
        api_response = api_instance.post_custom_field_post(property_id=property_id, name=name, shortcode=shortcode, apply_to=apply_to, required=required, max_characters=max_characters, type=type, displayed=displayed, is_personal=is_personal)
        print("The response of CustomFieldsApi->post_custom_field_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->post_custom_field_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **name** | **str**| Field name | [optional] 
 **shortcode** | **str**| Internal reference and is used for integration purposes such as custom links and the API | [optional] 
 **apply_to** | **str**| Where put this field in reservation or guest section of the booking. reservation - applies the custom field to reservations in myfrontdesk guest - applies the custom field to guest interface in myfrontdesk | [optional] [default to reservation]
 **required** | **bool**| Specify whether this field is required to be filled out. | [optional] [default to False]
 **max_characters** | **int**| Maximum number of characters allowed to be entered in this field. | [optional] [default to 40]
 **type** | **str**| The field&#39;s input type. | [optional] [default to input]
 **displayed** | [**List[str]**](str.md)| ¹ Specify where this custom field to show up. reservation - applies the custom field to reservation interface in myfrontdesk booking - applies the custom field to the booking engine card - applies the custom field to Registration cards | [optional] 
 **is_personal** | **bool**| Specifies if the contents of this field may contain personal information. User&#39;s personal information may be removed upon request according to GDPR rules. | [optional] 

### Return type

[**PostCustomFieldResponse**](PostCustomFieldResponse.md)

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

