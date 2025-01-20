# GetSourcesResponseDataInnerFeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_id** | **int** | ID of fee | [optional] 
**name** | **str** | Name of fee | [optional] 
**amount** | **float** | Value of fee | [optional] 
**amount_type** | **str** | If fee is percentage of amount or fixed | [optional] 
**type** | **str** | If fee is included or not in final price | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_sources_response_data_inner_fees_inner import GetSourcesResponseDataInnerFeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSourcesResponseDataInnerFeesInner from a JSON string
get_sources_response_data_inner_fees_inner_instance = GetSourcesResponseDataInnerFeesInner.from_json(json)
# print the JSON string representation of the object
print(GetSourcesResponseDataInnerFeesInner.to_json())

# convert the object into a dict
get_sources_response_data_inner_fees_inner_dict = get_sources_response_data_inner_fees_inner_instance.to_dict()
# create an instance of GetSourcesResponseDataInnerFeesInner from a dict
get_sources_response_data_inner_fees_inner_from_dict = GetSourcesResponseDataInnerFeesInner.from_dict(get_sources_response_data_inner_fees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


