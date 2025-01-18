# PutHouseAccountStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.put_house_account_status_response import PutHouseAccountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutHouseAccountStatusResponse from a JSON string
put_house_account_status_response_instance = PutHouseAccountStatusResponse.from_json(json)
# print the JSON string representation of the object
print(PutHouseAccountStatusResponse.to_json())

# convert the object into a dict
put_house_account_status_response_dict = put_house_account_status_response_instance.to_dict()
# create an instance of PutHouseAccountStatusResponse from a dict
put_house_account_status_response_from_dict = PutHouseAccountStatusResponse.from_dict(put_house_account_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


