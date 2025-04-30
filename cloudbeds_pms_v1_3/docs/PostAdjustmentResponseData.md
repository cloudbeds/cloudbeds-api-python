# PostAdjustmentResponseData

post Adjustment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_id** | **str** | Adjustment transaction identifier | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_adjustment_response_data import PostAdjustmentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostAdjustmentResponseData from a JSON string
post_adjustment_response_data_instance = PostAdjustmentResponseData.from_json(json)
# print the JSON string representation of the object
print(PostAdjustmentResponseData.to_json())

# convert the object into a dict
post_adjustment_response_data_dict = post_adjustment_response_data_instance.to_dict()
# create an instance of PostAdjustmentResponseData from a dict
post_adjustment_response_data_from_dict = PostAdjustmentResponseData.from_dict(post_adjustment_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


