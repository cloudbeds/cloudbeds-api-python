# PostGratuityRequestSchema

Request body for the standalone postGratuity endpoint (a tip with no check). Exactly one of reservationId / houseAccountId / eventCode must be provided. Sub-reservation routing is per-gratuity via GratuitySchema.subReservationId. To link tips to a check, use POST /folio/v1/checks/{checkId}/gratuities instead — checkId / checkNumber / POS context are check attributes and are not accepted here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation identifier. Required if houseAccountId and eventCode are not provided. | [optional] 
**house_account_id** | **str** | House account identifier. Required if reservationId and eventCode are not provided. | [optional] 
**event_code** | **str** | Event code. Required if reservationId and houseAccountId are not provided. | [optional] 
**folio_id** | **str** | Folio identifier within the chosen account target. Numeric string (the underlying folio_id is a 64-bit unsigned integer). Optional — when omitted, the default folio for the target is used. | [optional] 
**gratuities** | [**List[GratuitySchema]**](GratuitySchema.md) | Gratuity entries to post. At least one entry required. Each entry becomes its own folio line item and its own Accounting Service transaction. | 

## Example

```python
from cloudbeds_pms.models.post_gratuity_request_schema import PostGratuityRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostGratuityRequestSchema from a JSON string
post_gratuity_request_schema_instance = PostGratuityRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PostGratuityRequestSchema.to_json())

# convert the object into a dict
post_gratuity_request_schema_dict = post_gratuity_request_schema_instance.to_dict()
# create an instance of PostGratuityRequestSchema from a dict
post_gratuity_request_schema_from_dict = PostGratuityRequestSchema.from_dict(post_gratuity_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


