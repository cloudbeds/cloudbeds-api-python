# GetTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetTransactionsResponseDataInner]**](GetTransactionsResponseDataInner.md) | Transaction list covering the date range specified | [optional] 
**count** | **int** | Number of results returned, based on pagination and filter parameters | [optional] 
**total** | **int** | Total count of results, based on filter parameters | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_transactions_response import GetTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponse from a JSON string
get_transactions_response_instance = GetTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponse.to_json())

# convert the object into a dict
get_transactions_response_dict = get_transactions_response_instance.to_dict()
# create an instance of GetTransactionsResponse from a dict
get_transactions_response_from_dict = GetTransactionsResponse.from_dict(get_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


