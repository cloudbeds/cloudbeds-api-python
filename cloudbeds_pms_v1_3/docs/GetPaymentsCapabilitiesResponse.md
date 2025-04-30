# GetPaymentsCapabilitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetPaymentsCapabilitiesResponseDataInner]**](GetPaymentsCapabilitiesResponseDataInner.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payments_capabilities_response import GetPaymentsCapabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsCapabilitiesResponse from a JSON string
get_payments_capabilities_response_instance = GetPaymentsCapabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsCapabilitiesResponse.to_json())

# convert the object into a dict
get_payments_capabilities_response_dict = get_payments_capabilities_response_instance.to_dict()
# create an instance of GetPaymentsCapabilitiesResponse from a dict
get_payments_capabilities_response_from_dict = GetPaymentsCapabilitiesResponse.from_dict(get_payments_capabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


