# GetRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetRateResponseData**](GetRateResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_rate_response import GetRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateResponse from a JSON string
get_rate_response_instance = GetRateResponse.from_json(json)
# print the JSON string representation of the object
print(GetRateResponse.to_json())

# convert the object into a dict
get_rate_response_dict = get_rate_response_instance.to_dict()
# create an instance of GetRateResponse from a dict
get_rate_response_from_dict = GetRateResponse.from_dict(get_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


