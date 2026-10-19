# PutIntervalRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Interval start date (YYYY-MM-DD). | 
**end_date** | **str** | Interval end date (YYYY-MM-DD), inclusive. | 
**amount_allotted_for_sale** | **int** | New amount allotted for sale (&gt;&#x3D; 0). | 

## Example

```python
from cloudbeds_pms.models.put_interval_request_schema import PutIntervalRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PutIntervalRequestSchema from a JSON string
put_interval_request_schema_instance = PutIntervalRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PutIntervalRequestSchema.to_json())

# convert the object into a dict
put_interval_request_schema_dict = put_interval_request_schema_instance.to_dict()
# create an instance of PutIntervalRequestSchema from a dict
put_interval_request_schema_from_dict = PutIntervalRequestSchema.from_dict(put_interval_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


