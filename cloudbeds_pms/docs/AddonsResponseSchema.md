# AddonsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Number of results to skip | 
**limit** | **int** | Maximum number of results to return | 
**data** | [**List[AddonResponseSchema]**](AddonResponseSchema.md) | Contains the list of add-on details | 

## Example

```python
from cloudbeds_pms.models.addons_response_schema import AddonsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsResponseSchema from a JSON string
addons_response_schema_instance = AddonsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AddonsResponseSchema.to_json())

# convert the object into a dict
addons_response_schema_dict = addons_response_schema_instance.to_dict()
# create an instance of AddonsResponseSchema from a dict
addons_response_schema_from_dict = AddonsResponseSchema.from_dict(addons_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


