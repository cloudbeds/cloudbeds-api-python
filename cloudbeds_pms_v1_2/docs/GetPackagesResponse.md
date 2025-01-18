# GetPackagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetPackagesResponseData**](GetPackagesResponseData.md) |  | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_packages_response import GetPackagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPackagesResponse from a JSON string
get_packages_response_instance = GetPackagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPackagesResponse.to_json())

# convert the object into a dict
get_packages_response_dict = get_packages_response_instance.to_dict()
# create an instance of GetPackagesResponse from a dict
get_packages_response_from_dict = GetPackagesResponse.from_dict(get_packages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


