# LengthOfStaySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | **str** | How length-of-stay rules are applied. \&quot;progressive_application\&quot; applies per-night based on which night it is. \&quot;retroactive_adjustment\&quot; applies uniformly based on total stay length. | 
**ranges** | [**List[LengthOfStayRangeSchema]**](LengthOfStayRangeSchema.md) | Length-of-stay ranges. Each range defines amount overrides for a night count bracket. | 

## Example

```python
from cloudbeds_pms.models.length_of_stay_schema import LengthOfStaySchema

# TODO update the JSON string below
json = "{}"
# create an instance of LengthOfStaySchema from a JSON string
length_of_stay_schema_instance = LengthOfStaySchema.from_json(json)
# print the JSON string representation of the object
print(LengthOfStaySchema.to_json())

# convert the object into a dict
length_of_stay_schema_dict = length_of_stay_schema_instance.to_dict()
# create an instance of LengthOfStaySchema from a dict
length_of_stay_schema_from_dict = LengthOfStaySchema.from_dict(length_of_stay_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


