# CursorPaginationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 1000) | [optional] [default to 5]
**page_token** | **str** | Token to retrieve the next page of results. It is returned in the response of the previous page. | [optional] 

## Example

```python
from cloudbeds_pms.models.cursor_pagination_schema import CursorPaginationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaginationSchema from a JSON string
cursor_pagination_schema_instance = CursorPaginationSchema.from_json(json)
# print the JSON string representation of the object
print(CursorPaginationSchema.to_json())

# convert the object into a dict
cursor_pagination_schema_dict = cursor_pagination_schema_instance.to_dict()
# create an instance of CursorPaginationSchema from a dict
cursor_pagination_schema_from_dict = CursorPaginationSchema.from_dict(cursor_pagination_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


