# cloudbeds_pms_v1_3.AllotmentBlocksApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allotment_block_notes_post**](AllotmentBlocksApi.md#create_allotment_block_notes_post) | **POST** /createAllotmentBlockNotes | createAllotmentBlockNotes
[**create_allotment_block_post**](AllotmentBlocksApi.md#create_allotment_block_post) | **POST** /createAllotmentBlock | createAllotmentBlock
[**delete_allotment_block_post**](AllotmentBlocksApi.md#delete_allotment_block_post) | **POST** /deleteAllotmentBlock | deleteAllotmentBlock
[**get_allotment_blocks_get**](AllotmentBlocksApi.md#get_allotment_blocks_get) | **GET** /getAllotmentBlocks | getAllotmentBlocks
[**list_allotment_block_notes_get**](AllotmentBlocksApi.md#list_allotment_block_notes_get) | **GET** /listAllotmentBlockNotes | listAllotmentBlockNotes
[**update_allotment_block_notes_post**](AllotmentBlocksApi.md#update_allotment_block_notes_post) | **POST** /updateAllotmentBlockNotes | updateAllotmentBlockNotes
[**update_allotment_block_post**](AllotmentBlocksApi.md#update_allotment_block_post) | **POST** /updateAllotmentBlock | updateAllotmentBlock


# **create_allotment_block_notes_post**
> PostCreateAllotmentBlockNotesResponse create_allotment_block_notes_post(property_id=property_id, allotment_block_code=allotment_block_code, text=text)

createAllotmentBlockNotes

Add a note to an allotment block

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_create_allotment_block_notes_response import PostCreateAllotmentBlockNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    allotment_block_code = 'allotment_block_code_example' # str | Allotment Block Code (optional)
    text = 'text_example' # str | Note's text (optional)

    try:
        # createAllotmentBlockNotes
        api_response = api_instance.create_allotment_block_notes_post(property_id=property_id, allotment_block_code=allotment_block_code, text=text)
        print("The response of AllotmentBlocksApi->create_allotment_block_notes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->create_allotment_block_notes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **allotment_block_code** | **str**| Allotment Block Code | [optional] 
 **text** | **str**| Note&#39;s text | [optional] 

### Return type

[**PostCreateAllotmentBlockNotesResponse**](PostCreateAllotmentBlockNotesResponse.md)

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

# **create_allotment_block_post**
> PostCreateAllotmentBlockResponse create_allotment_block_post(group_code=group_code, allotment_block_name=allotment_block_name, rate_type=rate_type, rate_plan_id=rate_plan_id, allotment_type=allotment_type, allotment_block_status=allotment_block_status, allow_overbooking=allow_overbooking, auto_release=auto_release, allotment_intervals=allotment_intervals)

createAllotmentBlock

Retreive allotment blocks @apiQuery {Integer} propertyID Property ID

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_allotment_intervals_inner import PostCreateAllotmentBlockRequestAllotmentIntervalsInner
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_auto_release import PostCreateAllotmentBlockRequestAutoRelease
from cloudbeds_pms_v1_3.models.post_create_allotment_block_response import PostCreateAllotmentBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    group_code = 'group_code_example' # str | The unique identifier of the group profile the allotment block should be created (optional)
    allotment_block_name = 'allotment_block_name_example' # str | The name for the allotment block (optional)
    rate_type = 'rate_type_example' # str | The rate type for the associated intervals (optional)
    rate_plan_id = 'rate_plan_id_example' # str | The rate plan ID. Required if rateType is \\\"rate_plan\\\". (optional)
    allotment_type = 'allotment_type_example' # str | The allotment type (optional)
    allotment_block_status = 'allotment_block_status_example' # str | The status for the allotment block under (optional)
    allow_overbooking = True # bool | If false, or omitted, then this command will fail if it would result in an overbooking.  If true, then the update will succeed even if it results in an overbooking. (optional)
    auto_release = cloudbeds_pms_v1_3.PostCreateAllotmentBlockRequestAutoRelease() # PostCreateAllotmentBlockRequestAutoRelease |  (optional)
    allotment_intervals = [cloudbeds_pms_v1_3.PostCreateAllotmentBlockRequestAllotmentIntervalsInner()] # List[PostCreateAllotmentBlockRequestAllotmentIntervalsInner] | The day-based data for the allotment block. (optional)

    try:
        # createAllotmentBlock
        api_response = api_instance.create_allotment_block_post(group_code=group_code, allotment_block_name=allotment_block_name, rate_type=rate_type, rate_plan_id=rate_plan_id, allotment_type=allotment_type, allotment_block_status=allotment_block_status, allow_overbooking=allow_overbooking, auto_release=auto_release, allotment_intervals=allotment_intervals)
        print("The response of AllotmentBlocksApi->create_allotment_block_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->create_allotment_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_code** | **str**| The unique identifier of the group profile the allotment block should be created | [optional] 
 **allotment_block_name** | **str**| The name for the allotment block | [optional] 
 **rate_type** | **str**| The rate type for the associated intervals | [optional] 
 **rate_plan_id** | **str**| The rate plan ID. Required if rateType is \\\&quot;rate_plan\\\&quot;. | [optional] 
 **allotment_type** | **str**| The allotment type | [optional] 
 **allotment_block_status** | **str**| The status for the allotment block under | [optional] 
 **allow_overbooking** | **bool**| If false, or omitted, then this command will fail if it would result in an overbooking.  If true, then the update will succeed even if it results in an overbooking. | [optional] 
 **auto_release** | [**PostCreateAllotmentBlockRequestAutoRelease**](PostCreateAllotmentBlockRequestAutoRelease.md)|  | [optional] 
 **allotment_intervals** | [**List[PostCreateAllotmentBlockRequestAllotmentIntervalsInner]**](PostCreateAllotmentBlockRequestAllotmentIntervalsInner.md)| The day-based data for the allotment block. | [optional] 

### Return type

[**PostCreateAllotmentBlockResponse**](PostCreateAllotmentBlockResponse.md)

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

# **delete_allotment_block_post**
> PostDeleteAllotmentBlockResponse delete_allotment_block_post(allotment_block_code=allotment_block_code)

deleteAllotmentBlock

Delete allotment blocks

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_delete_allotment_block_response import PostDeleteAllotmentBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    allotment_block_code = 'allotment_block_code_example' # str | The unique code of the allotment Block (optional)

    try:
        # deleteAllotmentBlock
        api_response = api_instance.delete_allotment_block_post(allotment_block_code=allotment_block_code)
        print("The response of AllotmentBlocksApi->delete_allotment_block_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->delete_allotment_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allotment_block_code** | **str**| The unique code of the allotment Block | [optional] 

### Return type

[**PostDeleteAllotmentBlockResponse**](PostDeleteAllotmentBlockResponse.md)

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

# **get_allotment_blocks_get**
> GetAllotmentBlocksResponse get_allotment_blocks_get(property_id, allotment_block_code=allotment_block_code, allotment_block_name=allotment_block_name, group_code=group_code, allotment_block_status=allotment_block_status, allotment_block_type=allotment_block_type, room_type_id=room_type_id, page_size=page_size, page_number=page_number, start_date=start_date, end_date=end_date)

getAllotmentBlocks

Retrieve allotment blocks

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_allotment_blocks_response import GetAllotmentBlocksResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional, by default all authorized properties will be included)
    allotment_block_code = 'allotment_block_code_example' # str | Allotment block code (optional)
    allotment_block_name = 'allotment_block_name_example' # str | Allotment block name (optional)
    group_code = 'group_code_example' # str | A group profile code (optional)
    allotment_block_status = 'allotment_block_status_example' # str | Allotment block status(es) (optional)
    allotment_block_type = 'allotment_block_type_example' # str | The type of allotment block (optional)
    room_type_id = 'room_type_id_example' # str | Filters allotment blocks with the supplied Room Type ID. (optional)
    page_size = 56 # int | Number of allotment blocks to return per page (min: 1, max: 100) (optional)
    page_number = 56 # int | Which page in the results to access (optional)
    start_date = '2013-10-20' # date | Interval start date (optional)
    end_date = '2013-10-20' # date | Interval start date (optional)

    try:
        # getAllotmentBlocks
        api_response = api_instance.get_allotment_blocks_get(property_id, allotment_block_code=allotment_block_code, allotment_block_name=allotment_block_name, group_code=group_code, allotment_block_status=allotment_block_status, allotment_block_type=allotment_block_type, room_type_id=room_type_id, page_size=page_size, page_number=page_number, start_date=start_date, end_date=end_date)
        print("The response of AllotmentBlocksApi->get_allotment_blocks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->get_allotment_blocks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID (optional, by default all authorized properties will be included) | 
 **allotment_block_code** | **str**| Allotment block code | [optional] 
 **allotment_block_name** | **str**| Allotment block name | [optional] 
 **group_code** | **str**| A group profile code | [optional] 
 **allotment_block_status** | **str**| Allotment block status(es) | [optional] 
 **allotment_block_type** | **str**| The type of allotment block | [optional] 
 **room_type_id** | **str**| Filters allotment blocks with the supplied Room Type ID. | [optional] 
 **page_size** | **int**| Number of allotment blocks to return per page (min: 1, max: 100) | [optional] 
 **page_number** | **int**| Which page in the results to access | [optional] 
 **start_date** | **date**| Interval start date | [optional] 
 **end_date** | **date**| Interval start date | [optional] 

### Return type

[**GetAllotmentBlocksResponse**](GetAllotmentBlocksResponse.md)

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

# **list_allotment_block_notes_get**
> GetListAllotmentBlockNotesResponse list_allotment_block_notes_get(property_id, allotment_block_code, status=status, page_number=page_number, page_size=page_size)

listAllotmentBlockNotes

List notes added to an allotment block

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_list_allotment_block_notes_response import GetListAllotmentBlockNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    property_id = 'property_id_example' # str | Property ID
    allotment_block_code = 'allotment_block_code_example' # str | Allotment block code
    status = 'status_example' # str | Note status (optional)
    page_number = 56 # int | Page (optional)
    page_size = 56 # int | Number of Items per Page (min 1, max 100) (optional)

    try:
        # listAllotmentBlockNotes
        api_response = api_instance.list_allotment_block_notes_get(property_id, allotment_block_code, status=status, page_number=page_number, page_size=page_size)
        print("The response of AllotmentBlocksApi->list_allotment_block_notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->list_allotment_block_notes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | 
 **allotment_block_code** | **str**| Allotment block code | 
 **status** | **str**| Note status | [optional] 
 **page_number** | **int**| Page | [optional] 
 **page_size** | **int**| Number of Items per Page (min 1, max 100) | [optional] 

### Return type

[**GetListAllotmentBlockNotesResponse**](GetListAllotmentBlockNotesResponse.md)

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

# **update_allotment_block_notes_post**
> PostUpdateAllotmentBlockNotesResponse update_allotment_block_notes_post(property_id=property_id, allotment_block_code=allotment_block_code, note_id=note_id, text=text, status=status)

updateAllotmentBlockNotes

Update a note on an allotment block

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_update_allotment_block_notes_response import PostUpdateAllotmentBlockNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    allotment_block_code = 'allotment_block_code_example' # str | Allotment Block Code (optional)
    note_id = 'note_id_example' # str | Note's ID (optional)
    text = 'text_example' # str | Note's text (null for no change) (optional)
    status = 'status_example' # str | Note status (optional)

    try:
        # updateAllotmentBlockNotes
        api_response = api_instance.update_allotment_block_notes_post(property_id=property_id, allotment_block_code=allotment_block_code, note_id=note_id, text=text, status=status)
        print("The response of AllotmentBlocksApi->update_allotment_block_notes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->update_allotment_block_notes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **allotment_block_code** | **str**| Allotment Block Code | [optional] 
 **note_id** | **str**| Note&#39;s ID | [optional] 
 **text** | **str**| Note&#39;s text (null for no change) | [optional] 
 **status** | **str**| Note status | [optional] 

### Return type

[**PostUpdateAllotmentBlockNotesResponse**](PostUpdateAllotmentBlockNotesResponse.md)

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

# **update_allotment_block_post**
> PostUpdateAllotmentBlockResponse update_allotment_block_post(allotment_block_code=allotment_block_code, allotment_block_name=allotment_block_name, allow_overbooking=allow_overbooking, allotment_type=allotment_type, allotment_block_status=allotment_block_status, auto_release=auto_release, allotment_intervals=allotment_intervals)

updateAllotmentBlock

Update an allotment block @apiQuery {Integer} propertyID Property ID

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_update_allotment_block_request_allotment_intervals_inner import PostUpdateAllotmentBlockRequestAllotmentIntervalsInner
from cloudbeds_pms_v1_3.models.post_update_allotment_block_request_auto_release import PostUpdateAllotmentBlockRequestAutoRelease
from cloudbeds_pms_v1_3.models.post_update_allotment_block_response import PostUpdateAllotmentBlockResponse
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
    api_instance = cloudbeds_pms_v1_3.AllotmentBlocksApi(api_client)
    allotment_block_code = 'allotment_block_code_example' # str | The allotment block code identifying the allotment block to update (optional)
    allotment_block_name = 'allotment_block_name_example' # str | The name for the allotment block (optional)
    allow_overbooking = True # bool | If false, or omitted, then this update will fail if it would result in an overbooking.  If true, then the update will succeed even if it results in an overbooking. (optional)
    allotment_type = 'allotment_type_example' # str | The allotment type (optional)
    allotment_block_status = 'allotment_block_status_example' # str | The status for the allotment block under (optional)
    auto_release = cloudbeds_pms_v1_3.PostUpdateAllotmentBlockRequestAutoRelease() # PostUpdateAllotmentBlockRequestAutoRelease |  (optional)
    allotment_intervals = [cloudbeds_pms_v1_3.PostUpdateAllotmentBlockRequestAllotmentIntervalsInner()] # List[PostUpdateAllotmentBlockRequestAllotmentIntervalsInner] | The day-based data for the allotment block. (optional)

    try:
        # updateAllotmentBlock
        api_response = api_instance.update_allotment_block_post(allotment_block_code=allotment_block_code, allotment_block_name=allotment_block_name, allow_overbooking=allow_overbooking, allotment_type=allotment_type, allotment_block_status=allotment_block_status, auto_release=auto_release, allotment_intervals=allotment_intervals)
        print("The response of AllotmentBlocksApi->update_allotment_block_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllotmentBlocksApi->update_allotment_block_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allotment_block_code** | **str**| The allotment block code identifying the allotment block to update | [optional] 
 **allotment_block_name** | **str**| The name for the allotment block | [optional] 
 **allow_overbooking** | **bool**| If false, or omitted, then this update will fail if it would result in an overbooking.  If true, then the update will succeed even if it results in an overbooking. | [optional] 
 **allotment_type** | **str**| The allotment type | [optional] 
 **allotment_block_status** | **str**| The status for the allotment block under | [optional] 
 **auto_release** | [**PostUpdateAllotmentBlockRequestAutoRelease**](PostUpdateAllotmentBlockRequestAutoRelease.md)|  | [optional] 
 **allotment_intervals** | [**List[PostUpdateAllotmentBlockRequestAllotmentIntervalsInner]**](PostUpdateAllotmentBlockRequestAllotmentIntervalsInner.md)| The day-based data for the allotment block. | [optional] 

### Return type

[**PostUpdateAllotmentBlockResponse**](PostUpdateAllotmentBlockResponse.md)

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

