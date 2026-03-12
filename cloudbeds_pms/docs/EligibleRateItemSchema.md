# EligibleRateItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the rate plan or room type. | 
**type** | **str** | Type of rate: \&quot;rate_plan\&quot; or \&quot;base_rate\&quot;. | 
**package_id** | **str** | Package/rate plan ID. Present only when type is \&quot;rate_plan\&quot;. | [optional] 
**room_type_id** | **str** | Room type ID. Present only when type is \&quot;base_rate\&quot;. | [optional] 
**policy_id** | **str** | Smart policy ID associated with this rate plan, if any. Always null for base rates. | [optional] 

## Example

```python
from cloudbeds_pms.models.eligible_rate_item_schema import EligibleRateItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleRateItemSchema from a JSON string
eligible_rate_item_schema_instance = EligibleRateItemSchema.from_json(json)
# print the JSON string representation of the object
print(EligibleRateItemSchema.to_json())

# convert the object into a dict
eligible_rate_item_schema_dict = eligible_rate_item_schema_instance.to_dict()
# create an instance of EligibleRateItemSchema from a dict
eligible_rate_item_schema_from_dict = EligibleRateItemSchema.from_dict(eligible_rate_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


