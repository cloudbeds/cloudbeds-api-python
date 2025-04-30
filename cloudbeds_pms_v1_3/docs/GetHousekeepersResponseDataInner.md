# GetHousekeepersResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**housekeeper_id** | **str** | Housekeeper ID | [optional] 
**name** | **str** | Housekeeper Name | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_housekeepers_response_data_inner import GetHousekeepersResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHousekeepersResponseDataInner from a JSON string
get_housekeepers_response_data_inner_instance = GetHousekeepersResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetHousekeepersResponseDataInner.to_json())

# convert the object into a dict
get_housekeepers_response_data_inner_dict = get_housekeepers_response_data_inner_instance.to_dict()
# create an instance of GetHousekeepersResponseDataInner from a dict
get_housekeepers_response_data_inner_from_dict = GetHousekeepersResponseDataInner.from_dict(get_housekeepers_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


