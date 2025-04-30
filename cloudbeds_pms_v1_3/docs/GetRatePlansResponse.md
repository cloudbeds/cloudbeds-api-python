# GetRatePlansResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetRatePlansResponseDataInner]**](GetRatePlansResponseDataInner.md) | Rates details | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_plans_response import GetRatePlansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRatePlansResponse from a JSON string
get_rate_plans_response_instance = GetRatePlansResponse.from_json(json)
# print the JSON string representation of the object
print(GetRatePlansResponse.to_json())

# convert the object into a dict
get_rate_plans_response_dict = get_rate_plans_response_instance.to_dict()
# create an instance of GetRatePlansResponse from a dict
get_rate_plans_response_from_dict = GetRatePlansResponse.from_dict(get_rate_plans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


