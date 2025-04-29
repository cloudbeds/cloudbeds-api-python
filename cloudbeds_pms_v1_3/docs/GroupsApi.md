# cloudbeds_pms_v1_3.GroupsApi

All URIs are relative to *https://api.cloudbeds.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_notes_get**](GroupsApi.md#get_group_notes_get) | **GET** /getGroupNotes | getGroupNotes
[**get_groups_get**](GroupsApi.md#get_groups_get) | **GET** /getGroups | getGroups
[**patch_group_post**](GroupsApi.md#patch_group_post) | **POST** /patchGroup | patchGroup
[**post_group_note_post**](GroupsApi.md#post_group_note_post) | **POST** /postGroupNote | postGroupNote
[**put_group_post**](GroupsApi.md#put_group_post) | **POST** /putGroup | putGroup


# **get_group_notes_get**
> GetGroupNotesResponse get_group_notes_get(property_id, group_code, page_size, page_number)

getGroupNotes

Returns group notes

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_group_notes_response import GetGroupNotesResponse
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
    api_instance = cloudbeds_pms_v1_3.GroupsApi(api_client)
    property_id = 'property_id_example' # str | Property ID
    group_code = 'group_code_example' # str | Group code
    page_size = 56 # int | Number of groups notes to return per page (min: 1, max: 100)
    page_number = 56 # int | Which page in the results to access

    try:
        # getGroupNotes
        api_response = api_instance.get_group_notes_get(property_id, group_code, page_size, page_number)
        print("The response of GroupsApi->get_group_notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_notes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | 
 **group_code** | **str**| Group code | 
 **page_size** | **int**| Number of groups notes to return per page (min: 1, max: 100) | 
 **page_number** | **int**| Which page in the results to access | 

### Return type

[**GetGroupNotesResponse**](GetGroupNotesResponse.md)

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

# **get_groups_get**
> GetGroupsResponse get_groups_get(property_id, group_code=group_code, type=type, status=status, created_from=created_from, created_to=created_to, page_size=page_size, page_number=page_number)

getGroups

Returns the groups for a property

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.get_groups_response import GetGroupsResponse
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
    api_instance = cloudbeds_pms_v1_3.GroupsApi(api_client)
    property_id = 'property_id_example' # str | Property ID
    group_code = 'group_code_example' # str | Unique ID for a group (optional)
    type = 'type_example' # str | The type of group (optional)
    status = 'status_example' # str | Group status (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Datetime (lower limit) to be queried (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Datetime (upper limit) to be queried (optional)
    page_size = 56 # int | Number of groups to return per page (min: 1, max: 100) (optional)
    page_number = 56 # int | Which page in the results to access (optional)

    try:
        # getGroups
        api_response = api_instance.get_groups_get(property_id, group_code=group_code, type=type, status=status, created_from=created_from, created_to=created_to, page_size=page_size, page_number=page_number)
        print("The response of GroupsApi->get_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | 
 **group_code** | **str**| Unique ID for a group | [optional] 
 **type** | **str**| The type of group | [optional] 
 **status** | **str**| Group status | [optional] 
 **created_from** | **datetime**| Datetime (lower limit) to be queried | [optional] 
 **created_to** | **datetime**| Datetime (upper limit) to be queried | [optional] 
 **page_size** | **int**| Number of groups to return per page (min: 1, max: 100) | [optional] 
 **page_number** | **int**| Which page in the results to access | [optional] 

### Return type

[**GetGroupsResponse**](GetGroupsResponse.md)

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

# **patch_group_post**
> PostPatchGroupResponse patch_group_post(group_code=group_code, property_id=property_id, name=name, type=type, status=status, source_id=source_id, address1=address1, address2=address2, city=city, zip=zip, state=state)

patchGroup

Updates an existing group with information provided. At least one information field is required for this call.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_patch_group_response import PostPatchGroupResponse
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
    api_instance = cloudbeds_pms_v1_3.GroupsApi(api_client)
    group_code = 'group_code_example' # str | code for a group (optional)
    property_id = 'property_id_example' # str | Property ID (optional)
    name = 'name_example' # str | Name for a group (optional)
    type = 'type_example' # str | The type of group (optional)
    status = 'status_example' # str | Group status (optional)
    source_id = 'source_id_example' # str | Source ID for a group (optional)
    address1 = 'address1_example' # str | Address line 1 for a group (optional)
    address2 = 'address2_example' # str | Address line 2 for a group (optional)
    city = 'city_example' # str | City for a group (optional)
    zip = 'zip_example' # str | Zip for a group (optional)
    state = 'state_example' # str | State for a group (optional)

    try:
        # patchGroup
        api_response = api_instance.patch_group_post(group_code=group_code, property_id=property_id, name=name, type=type, status=status, source_id=source_id, address1=address1, address2=address2, city=city, zip=zip, state=state)
        print("The response of GroupsApi->patch_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->patch_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_code** | **str**| code for a group | [optional] 
 **property_id** | **str**| Property ID | [optional] 
 **name** | **str**| Name for a group | [optional] 
 **type** | **str**| The type of group | [optional] 
 **status** | **str**| Group status | [optional] 
 **source_id** | **str**| Source ID for a group | [optional] 
 **address1** | **str**| Address line 1 for a group | [optional] 
 **address2** | **str**| Address line 2 for a group | [optional] 
 **city** | **str**| City for a group | [optional] 
 **zip** | **str**| Zip for a group | [optional] 
 **state** | **str**| State for a group | [optional] 

### Return type

[**PostPatchGroupResponse**](PostPatchGroupResponse.md)

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

# **post_group_note_post**
> PostGroupNoteResponse post_group_note_post(property_id=property_id, group_code=group_code, group_note=group_note)

postGroupNote

Adds a group note

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_group_note_response import PostGroupNoteResponse
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
    api_instance = cloudbeds_pms_v1_3.GroupsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    group_code = 'group_code_example' # str | Group code (optional)
    group_note = 'group_note_example' # str | Group note (optional)

    try:
        # postGroupNote
        api_response = api_instance.post_group_note_post(property_id=property_id, group_code=group_code, group_note=group_note)
        print("The response of GroupsApi->post_group_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->post_group_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **group_code** | **str**| Group code | [optional] 
 **group_note** | **str**| Group note | [optional] 

### Return type

[**PostGroupNoteResponse**](PostGroupNoteResponse.md)

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

# **put_group_post**
> PostPutGroupResponse put_group_post(property_id=property_id, name=name, type=type, status=status, commission_type=commission_type, source_id=source_id, address1=address1, address2=address2, city=city, zip=zip, state=state)

putGroup

Adds a group to the property. Please note that the default setting for 'Route to Group Folio' will be 'No,' and the 'Reservation Folio Configuration' will be set as the default folio configuration. You can edit these settings through the user interface (UI).

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (api_key):

```python
import cloudbeds_pms_v1_3
from cloudbeds_pms_v1_3.models.post_put_group_response import PostPutGroupResponse
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
    api_instance = cloudbeds_pms_v1_3.GroupsApi(api_client)
    property_id = 'property_id_example' # str | Property ID (optional)
    name = 'name_example' # str | Name for a group (optional)
    type = 'type_example' # str | The type of group (optional)
    status = 'status_example' # str | Group status (optional)
    commission_type = 'commission_type_example' # str | Commission Type (optional)
    source_id = 'source_id_example' # str | Source ID for a group (optional)
    address1 = 'address1_example' # str | Address line 1 for a group (optional)
    address2 = 'address2_example' # str | Address line 2 for a group (optional)
    city = 'city_example' # str | City for a group (optional)
    zip = 'zip_example' # str | Zip for a group (optional)
    state = 'state_example' # str | State for a group (optional)

    try:
        # putGroup
        api_response = api_instance.put_group_post(property_id=property_id, name=name, type=type, status=status, commission_type=commission_type, source_id=source_id, address1=address1, address2=address2, city=city, zip=zip, state=state)
        print("The response of GroupsApi->put_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->put_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_id** | **str**| Property ID | [optional] 
 **name** | **str**| Name for a group | [optional] 
 **type** | **str**| The type of group | [optional] 
 **status** | **str**| Group status | [optional] 
 **commission_type** | **str**| Commission Type | [optional] 
 **source_id** | **str**| Source ID for a group | [optional] 
 **address1** | **str**| Address line 1 for a group | [optional] 
 **address2** | **str**| Address line 2 for a group | [optional] 
 **city** | **str**| City for a group | [optional] 
 **zip** | **str**| Zip for a group | [optional] 
 **state** | **str**| State for a group | [optional] 

### Return type

[**PostPutGroupResponse**](PostPutGroupResponse.md)

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

