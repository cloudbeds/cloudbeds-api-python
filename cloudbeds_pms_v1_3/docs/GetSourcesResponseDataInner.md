# GetSourcesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property Id | [optional] 
**source_id** | **str** | Source Identifier | [optional] 
**source_name** | **str** | Source Name | [optional] 
**is_third_party** | **bool** | true if source is from third party | [optional] 
**status** | **bool** | true if source is active | [optional] 
**commission** | **float** | How much commission charged by source (in %) | [optional] 
**payment_collect** | **str** | Type of payment collect practiced by source | [optional] 
**taxes** | [**List[GetSourcesResponseDataInnerTaxesInner]**](GetSourcesResponseDataInnerTaxesInner.md) |  | [optional] 
**fees** | [**List[GetSourcesResponseDataInnerFeesInner]**](GetSourcesResponseDataInnerFeesInner.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_sources_response_data_inner import GetSourcesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSourcesResponseDataInner from a JSON string
get_sources_response_data_inner_instance = GetSourcesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetSourcesResponseDataInner.to_json())

# convert the object into a dict
get_sources_response_data_inner_dict = get_sources_response_data_inner_instance.to_dict()
# create an instance of GetSourcesResponseDataInner from a dict
get_sources_response_data_inner_from_dict = GetSourcesResponseDataInner.from_dict(get_sources_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


