# PreviewAdjustmentRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation ID to preview the adjustment for. | 
**adjustment** | [**PreviewAdjustmentInputSchema**](PreviewAdjustmentInputSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.preview_adjustment_request_schema import PreviewAdjustmentRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewAdjustmentRequestSchema from a JSON string
preview_adjustment_request_schema_instance = PreviewAdjustmentRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PreviewAdjustmentRequestSchema.to_json())

# convert the object into a dict
preview_adjustment_request_schema_dict = preview_adjustment_request_schema_instance.to_dict()
# create an instance of PreviewAdjustmentRequestSchema from a dict
preview_adjustment_request_schema_from_dict = PreviewAdjustmentRequestSchema.from_dict(preview_adjustment_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


