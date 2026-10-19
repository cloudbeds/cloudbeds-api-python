# StopSellIntervalSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Interval start date (YYYY-MM-DD). | 
**end_date** | **str** | Interval end date (YYYY-MM-DD), inclusive. | 
**stop_sell** | **bool** | Whether the rate plan is closed for sale (stop-sell) on these dates. | 

## Example

```python
from cloudbeds_pms.models.stop_sell_interval_schema import StopSellIntervalSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StopSellIntervalSchema from a JSON string
stop_sell_interval_schema_instance = StopSellIntervalSchema.from_json(json)
# print the JSON string representation of the object
print(StopSellIntervalSchema.to_json())

# convert the object into a dict
stop_sell_interval_schema_dict = stop_sell_interval_schema_instance.to_dict()
# create an instance of StopSellIntervalSchema from a dict
stop_sell_interval_schema_from_dict = StopSellIntervalSchema.from_dict(stop_sell_interval_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


