# PostGovernmentReceiptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_government_receipt_response import PostGovernmentReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGovernmentReceiptResponse from a JSON string
post_government_receipt_response_instance = PostGovernmentReceiptResponse.from_json(json)
# print the JSON string representation of the object
print(PostGovernmentReceiptResponse.to_json())

# convert the object into a dict
post_government_receipt_response_dict = post_government_receipt_response_instance.to_dict()
# create an instance of PostGovernmentReceiptResponse from a dict
post_government_receipt_response_from_dict = PostGovernmentReceiptResponse.from_dict(post_government_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


