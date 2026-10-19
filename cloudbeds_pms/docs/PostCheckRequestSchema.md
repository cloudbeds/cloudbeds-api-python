# PostCheckRequestSchema

Posts a completed POS check (e.g., F&B) to a guest folio, house account, or group profile. Replaces postCustomItem with first-class folio transactions enriched with hospitality POS context (check identity, revenue center, meal period, gratuity, service charge). All items, taxes, fees, gratuities, service charge, discounts, and payments in this request belong to the single check identified by checkNumber/checkId. Multi-check batching is not supported — issue a separate postCheck call per check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_number** | **str** | Partner-assigned check number visible on the customer receipt (e.g., POS terminal display number). Stored on each posted folio line and visible in the folio UI. Optional — when omitted, the server mints a Cloudbeds reference (cb-&lt;id&gt;) and returns it in the response so the partner can echo it back. | [optional] 
**check_id** | **str** | Partner-assigned durable external reference for the check (UUID or opaque string). Optional — when omitted, Cloudbeds generates one and returns it. Echoed on the response and used to void the check later. Must be unique among the property&#39;s active checks; a value released by a void can be reused. Letters, digits, and . _ ~ - only (addressed as a URL path segment for void). | [optional] 
**reservation_id** | **str** | Reservation identifier. Required if houseAccountId and eventCode are not provided. Per-item sub-reservation targeting is expressed via items[].subReservationId. | [optional] 
**house_account_id** | **str** | House account identifier. Required if reservationId and eventCode are not provided. | [optional] 
**event_code** | **str** | Event code. Required if reservationId and houseAccountId are not provided. | [optional] 
**folio_id** | **str** | Folio identifier within the chosen account target. Numeric string (the underlying folio_id is a 64-bit unsigned integer). Optional — when omitted, the default folio for the target is used. | [optional] 
**room_id** | **str** | Room identifier where the charge originated, when applicable. | [optional] 
**guest_id** | **str** | Guest identifier. Optional — used for guest-attributed POS reporting. | [optional] 
**guest_name** | **str** | Guest name as captured at the POS. Used when no guestId is provided. | [optional] 
**sale_date** | **str** | Sale date in RFC 3339 format. If not provided, the current timestamp is used. A future saleDate produces a &#39;pending&#39; transaction. | [optional] 
**pos_context** | [**PosContextSchema**](PosContextSchema.md) |  | [optional] 
**cover_count** | **int** | Number of guests on the check. Used for per-cover F&amp;B reporting. | [optional] 
**totals** | [**CheckTotalsSchema**](CheckTotalsSchema.md) |  | [optional] 
**items** | [**List[CheckItemRequestSchema]**](CheckItemRequestSchema.md) | Line items on the check. Each line is posted as a regular folio item, not a Custom Item. At least one of items[] or totals must be supplied — when items[] is empty, totals is required, and the server posts a single folio line carrying totals.totalItems. | [optional] 
**gratuities** | [**List[GratuitySchema]**](GratuitySchema.md) | Optional list of gratuities on the check. Each entry becomes its own folio line item and its own Accounting Service transaction. Use multiple entries when both AUTO_GRATUITY (system-applied) and TIP (voluntary) are present, or when several servers each receive a tip. Embedded gratuities use GratuitySchema (without posContext) — POS context (checkNumber, restaurantName, revenueCenter, mealPeriod, staffReference) is inherited from this parent check. | [optional] 
**service_charge** | [**CheckServiceChargeRequestSchema**](CheckServiceChargeRequestSchema.md) |  | [optional] 
**discounts** | [**List[CheckDiscountRequestSchema]**](CheckDiscountRequestSchema.md) | Optional discounts applied to the check. Each entry becomes a distinct (negative) folio line item. | [optional] 
**payments** | [**List[CheckPaymentRequestSchema]**](CheckPaymentRequestSchema.md) | Optional payments to register against the check at posting time. If provided, payFullBalance is ignored. | [optional] 
**pay_full_balance** | **bool** | If true, a cash payment is automatically registered for the full check total (items + taxes + fees + gratuity + service charge - discounts). Ignored when payments[] is provided. | [optional] 

## Example

```python
from cloudbeds_pms.models.post_check_request_schema import PostCheckRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostCheckRequestSchema from a JSON string
post_check_request_schema_instance = PostCheckRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PostCheckRequestSchema.to_json())

# convert the object into a dict
post_check_request_schema_dict = post_check_request_schema_instance.to_dict()
# create an instance of PostCheckRequestSchema from a dict
post_check_request_schema_from_dict = PostCheckRequestSchema.from_dict(post_check_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


