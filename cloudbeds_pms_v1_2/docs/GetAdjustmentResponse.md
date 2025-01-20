# GetAdjustmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetAdjustmentResponseData**](GetAdjustmentResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_adjustment_response import GetAdjustmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdjustmentResponse from a JSON string
get_adjustment_response_instance = GetAdjustmentResponse.from_json(json)
# print the JSON string representation of the object
print(GetAdjustmentResponse.to_json())

# convert the object into a dict
get_adjustment_response_dict = get_adjustment_response_instance.to_dict()
# create an instance of GetAdjustmentResponse from a dict
get_adjustment_response_from_dict = GetAdjustmentResponse.from_dict(get_adjustment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


