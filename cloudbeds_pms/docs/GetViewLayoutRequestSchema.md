# GetViewLayoutRequestSchema

Parameters for resolving a view into a layout.  `filters` and `date` travel together: a day-scoped filter (`busy`) needs the day it is evaluated against, while a structural one (`kind`) does not. `revision` selects a specific revision instead of the published resolution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**DynamicFilterSchema**](DynamicFilterSchema.md) |  | [optional] 
**view_id** | **str** | A reserved built-in id (&#x60;accommodation-type&#x60;, &#x60;alphabetical&#x60;) or a stored view key. | 
**revision** | **str** | Render a specific revision instead of the published resolution. Requires the manage permission when the revision is a draft. | [optional] 
**var_date** | **date** | The day day-scoped filters are evaluated against, &#x60;yyyy-MM-dd&#x60;. Required when such a filter is present (&#x60;busy&#x60;), ignored otherwise — &#x60;kind&#x60; is structural and needs no date. | [optional] 

## Example

```python
from cloudbeds_pms.models.get_view_layout_request_schema import GetViewLayoutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewLayoutRequestSchema from a JSON string
get_view_layout_request_schema_instance = GetViewLayoutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetViewLayoutRequestSchema.to_json())

# convert the object into a dict
get_view_layout_request_schema_dict = get_view_layout_request_schema_instance.to_dict()
# create an instance of GetViewLayoutRequestSchema from a dict
get_view_layout_request_schema_from_dict = GetViewLayoutRequestSchema.from_dict(get_view_layout_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


