# PostCardResponseData

Rates details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Card ID | [optional] 
**card_number** | **str** | Ending digits of the credit card | [optional] 
**card_type** | **str** | Abbreviated name of credit card type | [optional] 
**redirect_url** | **str** | null if no 3ds required | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_card_response_data import PostCardResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostCardResponseData from a JSON string
post_card_response_data_instance = PostCardResponseData.from_json(json)
# print the JSON string representation of the object
print(PostCardResponseData.to_json())

# convert the object into a dict
post_card_response_data_dict = post_card_response_data_instance.to_dict()
# create an instance of PostCardResponseData from a dict
post_card_response_data_from_dict = PostCardResponseData.from_dict(post_card_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


