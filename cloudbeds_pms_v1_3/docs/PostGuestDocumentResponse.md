# PostGuestDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 
**data** | [**PostGuestDocumentResponseData**](PostGuestDocumentResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_guest_document_response import PostGuestDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGuestDocumentResponse from a JSON string
post_guest_document_response_instance = PostGuestDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(PostGuestDocumentResponse.to_json())

# convert the object into a dict
post_guest_document_response_dict = post_guest_document_response_instance.to_dict()
# create an instance of PostGuestDocumentResponse from a dict
post_guest_document_response_from_dict = PostGuestDocumentResponse.from_dict(post_guest_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


