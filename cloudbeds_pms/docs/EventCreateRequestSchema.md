# EventCreateRequestSchema

Request body for creating a new event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Event name | 
**profile_id** | **str** | GPS Profile ID to link to this event | [optional] 
**status** | **str** | Event status (default: lead) | [optional] 
**source_id** | **str** | Source ID for the event booking source | 
**start_date** | **str** | Event start date (YYYY-MM-DD). NOTE: Informational only - effective event dates are calculated from linked reservations. | [optional] 
**end_date** | **str** | Event end date (YYYY-MM-DD). NOTE: Informational only - effective event dates are calculated from linked reservations. | [optional] 
**transaction_mode** | **str** | Transaction routing mode (default: none) | [optional] 
**transaction_types** | **List[str]** | Transaction types to route (required when transactionMode is post_into_group). Matched exactly. Unknown values are stored but never match a transaction. Values by group. Room revenue: rate, roomRevenue_cancellation, roomRevenue_no_show, roomRevenue_manual. By identifier: &#x60;product_&lt;itemID&gt;&#x60; from getItems, &#x60;tax_&lt;taxID&gt;&#x60; and &#x60;fee_&lt;feeID&gt;&#x60; from getTaxesAndFees, &#x60;addon_&lt;id&gt;&#x60;, &#x60;custom_item_&lt;id&gt;&#x60;, &#x60;bookable_resource_&lt;resourceTypeID&gt;&#x60;. Other: channel_commission, accountsReceivable. Payments: the payment method &#x60;code&#x60; from getPaymentMethods, e.g. cash, cards, check (debit card), check_true (check), ebanking, pay_pal, terminal. Card brands: &#x60;cards_&lt;cardCode&gt;&#x60; and &#x60;terminal_&lt;cardCode&gt;&#x60; with cardCode from getPaymentMethods. Bare cards and terminal match only payments recorded without a brand. | [optional] 
**folio_config_id** | **str** | Folio configuration ID | [optional] 
**enable_aggregate_allotment_block** | **bool** | Enable aggregate allotment block feature | [optional] 
**aggregate_allotment_block_package_id** | **str** | Package ID for aggregate allotment block | [optional] 
**segment_id** | **str** | Market segment ID | [optional] 

## Example

```python
from cloudbeds_pms.models.event_create_request_schema import EventCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventCreateRequestSchema from a JSON string
event_create_request_schema_instance = EventCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventCreateRequestSchema.to_json())

# convert the object into a dict
event_create_request_schema_dict = event_create_request_schema_instance.to_dict()
# create an instance of EventCreateRequestSchema from a dict
event_create_request_schema_from_dict = EventCreateRequestSchema.from_dict(event_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


