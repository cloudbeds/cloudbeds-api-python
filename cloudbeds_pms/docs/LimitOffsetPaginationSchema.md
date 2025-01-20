# LimitOffsetPaginationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]

## Example

```python
from cloudbeds_pms.models.limit_offset_pagination_schema import LimitOffsetPaginationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPaginationSchema from a JSON string
limit_offset_pagination_schema_instance = LimitOffsetPaginationSchema.from_json(json)
# print the JSON string representation of the object
print(LimitOffsetPaginationSchema.to_json())

# convert the object into a dict
limit_offset_pagination_schema_dict = limit_offset_pagination_schema_instance.to_dict()
# create an instance of LimitOffsetPaginationSchema from a dict
limit_offset_pagination_schema_from_dict = LimitOffsetPaginationSchema.from_dict(limit_offset_pagination_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


