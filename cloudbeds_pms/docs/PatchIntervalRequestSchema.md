# PatchIntervalRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Interval start date (YYYY-MM-DD). | 
**end_date** | **str** | Interval end date (YYYY-MM-DD), inclusive. | 
**amount_allotted_for_sale_delta** | **int** | Relative change (must be non-zero; may be negative; result is floored at 0). | 

## Example

```python
from cloudbeds_pms.models.patch_interval_request_schema import PatchIntervalRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIntervalRequestSchema from a JSON string
patch_interval_request_schema_instance = PatchIntervalRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PatchIntervalRequestSchema.to_json())

# convert the object into a dict
patch_interval_request_schema_dict = patch_interval_request_schema_instance.to_dict()
# create an instance of PatchIntervalRequestSchema from a dict
patch_interval_request_schema_from_dict = PatchIntervalRequestSchema.from_dict(patch_interval_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


