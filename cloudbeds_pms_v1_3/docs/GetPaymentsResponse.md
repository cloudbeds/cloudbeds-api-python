# GetPaymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetPaymentsResponseDataInner]**](GetPaymentsResponseDataInner.md) | Transaction list | [optional] 
**count** | **int** | Number of results returned, based on pagination | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payments_response import GetPaymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsResponse from a JSON string
get_payments_response_instance = GetPaymentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsResponse.to_json())

# convert the object into a dict
get_payments_response_dict = get_payments_response_instance.to_dict()
# create an instance of GetPaymentsResponse from a dict
get_payments_response_from_dict = GetPaymentsResponse.from_dict(get_payments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


