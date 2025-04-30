# GetRoomsFeesAndTaxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetRoomsFeesAndTaxesResponseData**](GetRoomsFeesAndTaxesResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rooms_fees_and_taxes_response import GetRoomsFeesAndTaxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomsFeesAndTaxesResponse from a JSON string
get_rooms_fees_and_taxes_response_instance = GetRoomsFeesAndTaxesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRoomsFeesAndTaxesResponse.to_json())

# convert the object into a dict
get_rooms_fees_and_taxes_response_dict = get_rooms_fees_and_taxes_response_instance.to_dict()
# create an instance of GetRoomsFeesAndTaxesResponse from a dict
get_rooms_fees_and_taxes_response_from_dict = GetRoomsFeesAndTaxesResponse.from_dict(get_rooms_fees_and_taxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


