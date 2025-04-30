# PostGuestDocumentResponseData

Details for the uploaded file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | uploaded file identifier | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_guest_document_response_data import PostGuestDocumentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostGuestDocumentResponseData from a JSON string
post_guest_document_response_data_instance = PostGuestDocumentResponseData.from_json(json)
# print the JSON string representation of the object
print(PostGuestDocumentResponseData.to_json())

# convert the object into a dict
post_guest_document_response_data_dict = post_guest_document_response_data_instance.to_dict()
# create an instance of PostGuestDocumentResponseData from a dict
post_guest_document_response_data_from_dict = PostGuestDocumentResponseData.from_dict(post_guest_document_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


