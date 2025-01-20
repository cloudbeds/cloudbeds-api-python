# cloudbeds_pms_v1_2.HotelApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_files_get**](HotelApi.md#get_files_get) | **GET** /getFiles | getFiles
[**get_hotel_details_get**](HotelApi.md#get_hotel_details_get) | **GET** /getHotelDetails | getHotelDetails
[**get_hotels_get**](HotelApi.md#get_hotels_get) | **GET** /getHotels | getHotels
[**post_file_post**](HotelApi.md#post_file_post) | **POST** /postFile | postFile


# **get_files_get**
> GetFilesResponse get_files_get(property_id=property_id, sort_by=sort_by, order_by=order_by, name=name, page_number=page_number, page_size=page_size)

getFiles

Returns a list of files attached to a hotel, ordered by creation date

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_files_response import GetFilesResponse
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
    api_instance = cloudbeds_pms_v1_2.HotelApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    sort_by = date # str | Sort By parameter (optional) (default to date)
    order_by = desc # str | Order response in DESCending or ASCending order, used together with sortBy (optional) (default to desc)
    name = 'name_example' # str | Filter filess by name. Include only with names containing specified string (optional)
    page_number = 1 # int | Results page number (optional) (default to 1)
    page_size = 100 # int | Results page size. Max = 100 (optional) (default to 100)

    try:
        # getFiles
        api_response = api_instance.get_files_get(property_id=property_id, sort_by=sort_by, order_by=order_by, name=name, page_number=page_number, page_size=page_size)
        print("The response of HotelApi->get_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotelApi->get_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **sort_by** | **str**| Sort By parameter | [optional] [default to date]
 **order_by** | **str**| Order response in DESCending or ASCending order, used together with sortBy | [optional] [default to desc]
 **name** | **str**| Filter filess by name. Include only with names containing specified string | [optional] 
 **page_number** | **int**| Results page number | [optional] [default to 1]
 **page_size** | **int**| Results page size. Max &#x3D; 100 | [optional] [default to 100]

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

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

# **get_hotel_details_get**
> GetHotelDetailsResponse get_hotel_details_get(property_id=property_id)

getHotelDetails

Returns the details of a specific hotel, identified by \"propertyID\"

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_hotel_details_response import GetHotelDetailsResponse
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
    api_instance = cloudbeds_pms_v1_2.HotelApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)

    try:
        # getHotelDetails
        api_response = api_instance.get_hotel_details_get(property_id=property_id)
        print("The response of HotelApi->get_hotel_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotelApi->get_hotel_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 

### Return type

[**GetHotelDetailsResponse**](GetHotelDetailsResponse.md)

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

# **get_hotels_get**
> GetHotelsResponse get_hotels_get(property_ids=property_ids, property_name=property_name, property_city=property_city, page_number=page_number, page_size=page_size)

getHotels

Returns a list of hotels, filtered by the parameters passed ### Group account support

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.get_hotels_response import GetHotelsResponse
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
    api_instance = cloudbeds_pms_v1_2.HotelApi(api_client)
    property_ids = 'property_ids_example' # str | List of property IDs, comma-separated, i.e. 37,345,89 (optional)
    property_name = 'property_name_example' # str | Property name, or part of it (optional)
    property_city = 'property_city_example' # str | Property city, or part of it (optional)
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Page size (optional) (default to 20)

    try:
        # getHotels
        api_response = api_instance.get_hotels_get(property_ids=property_ids, property_name=property_name, property_city=property_city, page_number=page_number, page_size=page_size)
        print("The response of HotelApi->get_hotels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotelApi->get_hotels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_ids** | **str**| List of property IDs, comma-separated, i.e. 37,345,89 | [optional] 
 **property_name** | **str**| Property name, or part of it | [optional] 
 **property_city** | **str**| Property city, or part of it | [optional] 
 **page_number** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Page size | [optional] [default to 20]

### Return type

[**GetHotelsResponse**](GetHotelsResponse.md)

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

# **post_file_post**
> PostFileResponse post_file_post(property_id=property_id, file=file)

postFile

Attaches a file to a hotel

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_2
from cloudbeds_pms_v1_2.models.post_file_response import PostFileResponse
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
    api_instance = cloudbeds_pms_v1_2.HotelApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    file = None # bytearray | Form-based File Upload<br/> Allowed file types: <code>*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml</code><br/> Allowed max file size: 100MB (optional)

    try:
        # postFile
        api_response = api_instance.post_file_post(property_id=property_id, file=file)
        print("The response of HotelApi->post_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotelApi->post_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **file** | **bytearray**| Form-based File Upload&lt;br/&gt; Allowed file types: &lt;code&gt;*.pdf, *.rtf, *.doc, *.docx, *.txt, *.jpg, *.jpeg, *.png, *.gif, *.csv, *.xls, *.xlsx, *.xml&lt;/code&gt;&lt;br/&gt; Allowed max file size: 100MB | [optional] 

### Return type

[**PostFileResponse**](PostFileResponse.md)

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

