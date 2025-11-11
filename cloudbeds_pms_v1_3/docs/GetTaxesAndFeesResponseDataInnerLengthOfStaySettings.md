# GetTaxesAndFeesResponseDataInnerLengthOfStaySettings

Length of Stay configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | **str** | Application type for Length of Stay rules:&lt;br/&gt; &lt;table&gt; &lt;tr&gt;&lt;th&gt;Value&lt;/th&gt;&lt;th&gt;Meaning&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;progressive_application&lt;/td&gt;&lt;td&gt;Apply tax/fee when minimum nights are reached&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;retroactive_adjustment&lt;/td&gt;&lt;td&gt;Apply adjustments retroactively when conditions are met&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; | [optional] 
**ranges** | [**List[GetTaxesAndFeesResponseDataInnerLengthOfStaySettingsRangesInner]**](GetTaxesAndFeesResponseDataInnerLengthOfStaySettingsRangesInner.md) | Night-based ranges for Length of Stay configuration | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_taxes_and_fees_response_data_inner_length_of_stay_settings import GetTaxesAndFeesResponseDataInnerLengthOfStaySettings

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesAndFeesResponseDataInnerLengthOfStaySettings from a JSON string
get_taxes_and_fees_response_data_inner_length_of_stay_settings_instance = GetTaxesAndFeesResponseDataInnerLengthOfStaySettings.from_json(json)
# print the JSON string representation of the object
print(GetTaxesAndFeesResponseDataInnerLengthOfStaySettings.to_json())

# convert the object into a dict
get_taxes_and_fees_response_data_inner_length_of_stay_settings_dict = get_taxes_and_fees_response_data_inner_length_of_stay_settings_instance.to_dict()
# create an instance of GetTaxesAndFeesResponseDataInnerLengthOfStaySettings from a dict
get_taxes_and_fees_response_data_inner_length_of_stay_settings_from_dict = GetTaxesAndFeesResponseDataInnerLengthOfStaySettings.from_dict(get_taxes_and_fees_response_data_inner_length_of_stay_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


