# GetPaymentsCapabilitiesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudbeds_payments** | **bool** | If Cloudbeds Payments is enabled for this property | [optional] 
**terminal** | **bool** | If the property has an active terminal | [optional] 
**tap_to_pay** | **bool** | If tap-to-pay is enabled for the property in the backend gateway | [optional] 
**gateway** | **str** | The backend gateway in use for this property | [optional] 
**pay_by_link** | **bool** | If Pay-by-Link is enabled for the property | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payments_capabilities_response_data_inner import GetPaymentsCapabilitiesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsCapabilitiesResponseDataInner from a JSON string
get_payments_capabilities_response_data_inner_instance = GetPaymentsCapabilitiesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsCapabilitiesResponseDataInner.to_json())

# convert the object into a dict
get_payments_capabilities_response_data_inner_dict = get_payments_capabilities_response_data_inner_instance.to_dict()
# create an instance of GetPaymentsCapabilitiesResponseDataInner from a dict
get_payments_capabilities_response_data_inner_from_dict = GetPaymentsCapabilitiesResponseDataInner.from_dict(get_payments_capabilities_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


