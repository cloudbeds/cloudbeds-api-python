# CheckServiceChargeRequestSchema

Service charge associated with the check. Posted as a distinct folio line item, separate from items[] and gratuity. Reported and routed independently from food/beverage revenue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Service charge amount in the property currency. | 
**taxes** | [**List[TaxSchema]**](TaxSchema.md) | Tax rows applied to the service charge. Each row references a property-configured tax by ID. Schema reused from the Gratuity domain. | [optional] 
**custom_transaction_code** | **str** | Override the property&#39;s default service-charge Custom Transaction Code for this posting. If omitted, the property&#39;s configured default applies. | [optional] 
**general_ledger_custom_code** | **str** | Override the property&#39;s default service-charge General Ledger code for this posting. If omitted, the property&#39;s configured default applies. | [optional] 
**note** | **str** | Optional free-text note attached to the service charge line item. | [optional] 

## Example

```python
from cloudbeds_pms.models.check_service_charge_request_schema import CheckServiceChargeRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckServiceChargeRequestSchema from a JSON string
check_service_charge_request_schema_instance = CheckServiceChargeRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CheckServiceChargeRequestSchema.to_json())

# convert the object into a dict
check_service_charge_request_schema_dict = check_service_charge_request_schema_instance.to_dict()
# create an instance of CheckServiceChargeRequestSchema from a dict
check_service_charge_request_schema_from_dict = CheckServiceChargeRequestSchema.from_dict(check_service_charge_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


