# cloudbeds_pms.EventsApi

All URIs are relative to *https://api.cloudbeds.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_controller_create**](EventsApi.md#event_controller_create) | **POST** /events/v2/events | Create a new event
[**event_controller_destroy**](EventsApi.md#event_controller_destroy) | **DELETE** /events/v2/events/{eventId} | Delete an event
[**event_controller_list**](EventsApi.md#event_controller_list) | **GET** /events/v2/events | List events for a property
[**event_controller_show**](EventsApi.md#event_controller_show) | **GET** /events/v2/events/{eventId} | Get a single event
[**event_controller_update**](EventsApi.md#event_controller_update) | **PATCH** /events/v2/events/{eventId} | Update an existing event
[**event_note_controller_create**](EventsApi.md#event_note_controller_create) | **POST** /events/v2/events/{eventId}/notes | Create a note for an event
[**event_note_controller_list**](EventsApi.md#event_note_controller_list) | **GET** /events/v2/events/{eventId}/notes | List notes for an event
[**event_note_controller_update**](EventsApi.md#event_note_controller_update) | **PATCH** /events/v2/events/{eventId}/notes/{noteId} | Update an event note


# **event_controller_create**
> EventSingleResponseSchema event_controller_create(x_property_id, event_create_request_schema)

Create a new event

Creates a new event associated with an existing group profile or without any profile association.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_create_request_schema import EventCreateRequestSchema
from cloudbeds_pms.models.event_single_response_schema import EventSingleResponseSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_create_request_schema = cloudbeds_pms.EventCreateRequestSchema() # EventCreateRequestSchema | 

    try:
        # Create a new event
        api_response = api_instance.event_controller_create(x_property_id, event_create_request_schema)
        print("The response of EventsApi->event_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_create_request_schema** | [**EventCreateRequestSchema**](EventCreateRequestSchema.md)|  | 

### Return type

[**EventSingleResponseSchema**](EventSingleResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_controller_destroy**
> event_controller_destroy(x_property_id, event_id)

Delete an event

Deletes an event by ID or event code. This is a soft delete.

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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code

    try:
        # Delete an event
        api_instance.event_controller_destroy(x_property_id, event_id)
    except Exception as e:
        print("Exception when calling EventsApi->event_controller_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Event deleted |  -  |
**404** | Event not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_controller_list**
> EventListResponseSchema event_controller_list(x_property_id, event_code=event_code, profile_id=profile_id, status=status, created_from=created_from, created_to=created_to, start_date_from=start_date_from, start_date_to=start_date_to, end_date_from=end_date_from, end_date_to=end_date_to, limit=limit, offset=offset)

List events for a property

Returns a paginated list of events for a property. Events contain operational data and reference group profiles via profileId.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_list_response_schema import EventListResponseSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_code = 'event_code_example' # str |  (optional)
    profile_id = 'profile_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_date_from = '2013-10-20' # date |  (optional)
    start_date_to = '2013-10-20' # date |  (optional)
    end_date_from = '2013-10-20' # date |  (optional)
    end_date_to = '2013-10-20' # date |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List events for a property
        api_response = api_instance.event_controller_list(x_property_id, event_code=event_code, profile_id=profile_id, status=status, created_from=created_from, created_to=created_to, start_date_from=start_date_from, start_date_to=start_date_to, end_date_from=end_date_from, end_date_to=end_date_to, limit=limit, offset=offset)
        print("The response of EventsApi->event_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_controller_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_code** | **str**|  | [optional] 
 **profile_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **created_from** | **datetime**|  | [optional] 
 **created_to** | **datetime**|  | [optional] 
 **start_date_from** | **date**|  | [optional] 
 **start_date_to** | **date**|  | [optional] 
 **end_date_from** | **date**|  | [optional] 
 **end_date_to** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**EventListResponseSchema**](EventListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of events |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_controller_show**
> EventSingleResponseSchema event_controller_show(x_property_id, event_id)

Get a single event

Returns detailed information about a specific event.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_single_response_schema import EventSingleResponseSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code (e.g., \"12345\" or \"g162795\")

    try:
        # Get a single event
        api_response = api_instance.event_controller_show(x_property_id, event_id)
        print("The response of EventsApi->event_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_controller_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | 

### Return type

[**EventSingleResponseSchema**](EventSingleResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event details |  -  |
**404** | Event not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_controller_update**
> EventSingleResponseSchema event_controller_update(x_property_id, event_id, event_update_request_schema)

Update an existing event

Updates an event. Only provided fields are updated. For profileId: omit to keep, null to clear, string to replace.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_single_response_schema import EventSingleResponseSchema
from cloudbeds_pms.models.event_update_request_schema import EventUpdateRequestSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code
    event_update_request_schema = cloudbeds_pms.EventUpdateRequestSchema() # EventUpdateRequestSchema | 

    try:
        # Update an existing event
        api_response = api_instance.event_controller_update(x_property_id, event_id, event_update_request_schema)
        print("The response of EventsApi->event_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code | 
 **event_update_request_schema** | [**EventUpdateRequestSchema**](EventUpdateRequestSchema.md)|  | 

### Return type

[**EventSingleResponseSchema**](EventSingleResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event updated |  -  |
**400** | Bad request |  -  |
**404** | Event not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_note_controller_create**
> EventNoteSingleResponseSchema event_note_controller_create(x_property_id, event_id, event_note_create_request_schema)

Create a note for an event

Creates a new note for a specific event.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_note_create_request_schema import EventNoteCreateRequestSchema
from cloudbeds_pms.models.event_note_single_response_schema import EventNoteSingleResponseSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code
    event_note_create_request_schema = cloudbeds_pms.EventNoteCreateRequestSchema() # EventNoteCreateRequestSchema | 

    try:
        # Create a note for an event
        api_response = api_instance.event_note_controller_create(x_property_id, event_id, event_note_create_request_schema)
        print("The response of EventsApi->event_note_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_note_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code | 
 **event_note_create_request_schema** | [**EventNoteCreateRequestSchema**](EventNoteCreateRequestSchema.md)|  | 

### Return type

[**EventNoteSingleResponseSchema**](EventNoteSingleResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Note created |  -  |
**400** | Bad request |  -  |
**404** | Event not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_note_controller_list**
> EventNoteListResponseSchema event_note_controller_list(x_property_id, event_id, limit=limit, offset=offset, include_archived=include_archived)

List notes for an event

Returns a paginated list of notes for a specific event.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_note_list_response_schema import EventNoteListResponseSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    include_archived = False # bool |  (optional) (default to False)

    try:
        # List notes for an event
        api_response = api_instance.event_note_controller_list(x_property_id, event_id, limit=limit, offset=offset, include_archived=include_archived)
        print("The response of EventsApi->event_note_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_note_controller_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **include_archived** | **bool**|  | [optional] [default to False]

### Return type

[**EventNoteListResponseSchema**](EventNoteListResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of notes |  -  |
**404** | Event not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_note_controller_update**
> EventNoteSingleResponseSchema event_note_controller_update(x_property_id, event_id, note_id, event_note_update_request_schema)

Update an event note

Updates an existing note or archives it.

### Example

* OAuth Authentication (default):

```python
import cloudbeds_pms
from cloudbeds_pms.models.event_note_single_response_schema import EventNoteSingleResponseSchema
from cloudbeds_pms.models.event_note_update_request_schema import EventNoteUpdateRequestSchema
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
    api_instance = cloudbeds_pms.EventsApi(api_client)
    x_property_id = '1,2,3' # str | A numeric, comma-separated string representing the property IDs, sent in the header.
    event_id = 'event_id_example' # str | Event ID or event code
    note_id = 'note_id_example' # str | Note ID
    event_note_update_request_schema = cloudbeds_pms.EventNoteUpdateRequestSchema() # EventNoteUpdateRequestSchema | 

    try:
        # Update an event note
        api_response = api_instance.event_note_controller_update(x_property_id, event_id, note_id, event_note_update_request_schema)
        print("The response of EventsApi->event_note_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_note_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_property_id** | **str**| A numeric, comma-separated string representing the property IDs, sent in the header. | 
 **event_id** | **str**| Event ID or event code | 
 **note_id** | **str**| Note ID | 
 **event_note_update_request_schema** | [**EventNoteUpdateRequestSchema**](EventNoteUpdateRequestSchema.md)|  | 

### Return type

[**EventNoteSingleResponseSchema**](EventNoteSingleResponseSchema.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note updated |  -  |
**400** | Bad request |  -  |
**404** | Event or note not found |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

