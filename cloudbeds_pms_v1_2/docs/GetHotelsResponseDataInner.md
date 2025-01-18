# GetHotelsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**organization_id** | **str** | Organization ID | [optional] 
**property_name** | **str** | Property name | [optional] 
**property_image** | **str** | Property image URL | [optional] 
**property_description** | **str** | Property description | [optional] 
**property_timezone** | **str** | Property Timezone | [optional] 
**property_currency** | [**List[GetHotelsResponseDataInnerPropertyCurrencyInner]**](GetHotelsResponseDataInnerPropertyCurrencyInner.md) | Currency used by the property | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_hotels_response_data_inner import GetHotelsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelsResponseDataInner from a JSON string
get_hotels_response_data_inner_instance = GetHotelsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetHotelsResponseDataInner.to_json())

# convert the object into a dict
get_hotels_response_data_inner_dict = get_hotels_response_data_inner_instance.to_dict()
# create an instance of GetHotelsResponseDataInner from a dict
get_hotels_response_data_inner_from_dict = GetHotelsResponseDataInner.from_dict(get_hotels_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


