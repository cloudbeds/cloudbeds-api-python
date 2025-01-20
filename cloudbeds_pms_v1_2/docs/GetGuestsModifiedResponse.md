# GetGuestsModifiedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetGuestsModifiedResponseDataInner]**](GetGuestsModifiedResponseDataInner.md) | Details for the guest linked to the property | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_guests_modified_response import GetGuestsModifiedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestsModifiedResponse from a JSON string
get_guests_modified_response_instance = GetGuestsModifiedResponse.from_json(json)
# print the JSON string representation of the object
print(GetGuestsModifiedResponse.to_json())

# convert the object into a dict
get_guests_modified_response_dict = get_guests_modified_response_instance.to_dict()
# create an instance of GetGuestsModifiedResponse from a dict
get_guests_modified_response_from_dict = GetGuestsModifiedResponse.from_dict(get_guests_modified_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


