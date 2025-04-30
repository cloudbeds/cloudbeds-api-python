# PostPatchRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns true if the request could be completed | [optional] 
**job_reference_id** | **str** | ReferenceId ID for the job created for this update.  This can be used to track success of the batch for this rate update. See getRateJobs or the Rate Batch Job Webhook | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_patch_rate_response import PostPatchRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostPatchRateResponse from a JSON string
post_patch_rate_response_instance = PostPatchRateResponse.from_json(json)
# print the JSON string representation of the object
print(PostPatchRateResponse.to_json())

# convert the object into a dict
post_patch_rate_response_dict = post_patch_rate_response_instance.to_dict()
# create an instance of PostPatchRateResponse from a dict
post_patch_rate_response_from_dict = PostPatchRateResponse.from_dict(post_patch_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


