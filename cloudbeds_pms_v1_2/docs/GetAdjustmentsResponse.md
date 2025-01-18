# GetAdjustmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetAdjustmentsResponseData**](GetAdjustmentsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_adjustments_response import GetAdjustmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdjustmentsResponse from a JSON string
get_adjustments_response_instance = GetAdjustmentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAdjustmentsResponse.to_json())

# convert the object into a dict
get_adjustments_response_dict = get_adjustments_response_instance.to_dict()
# create an instance of GetAdjustmentsResponse from a dict
get_adjustments_response_from_dict = GetAdjustmentsResponse.from_dict(get_adjustments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


