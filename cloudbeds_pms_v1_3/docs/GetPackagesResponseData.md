# GetPackagesResponseData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_names** | **List[str]** | Array of package names | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_packages_response_data import GetPackagesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPackagesResponseData from a JSON string
get_packages_response_data_instance = GetPackagesResponseData.from_json(json)
# print the JSON string representation of the object
print(GetPackagesResponseData.to_json())

# convert the object into a dict
get_packages_response_data_dict = get_packages_response_data_instance.to_dict()
# create an instance of GetPackagesResponseData from a dict
get_packages_response_data_from_dict = GetPackagesResponseData.from_dict(get_packages_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


