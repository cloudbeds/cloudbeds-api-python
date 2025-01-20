# GetTransactionsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**reservation_id** | **str** | Reservation ID | [optional] 
**sub_reservation_id** | **str** | Sub Reservation ID | [optional] 
**house_account_id** | **str** | House Account ID | [optional] 
**house_account_name** | **str** | House Account Name | [optional] 
**guest_id** | **str** | Guest ID | [optional] 
**property_name** | **str** | Property Name | [optional] 
**transaction_date_time** | **datetime** | DateTime that the transaction was stored | [optional] 
**transaction_date_time_utc** | **datetime** | DateTime that the transaction was stored, in UTC timezone | [optional] 
**transaction_modified_date_time** | **datetime** | DateTime that the transaction was last modified | [optional] 
**transaction_modified_date_time_utc** | **datetime** | DateTime that the transaction was last modified, in UTC timezone | [optional] 
**guest_check_in** | **date** | Reservation Check-in date | [optional] 
**guest_check_out** | **date** | Reservation Check-out date | [optional] 
**room_type_id** | **str** | ID of the room type | [optional] 
**room_type_name** | **str** | Name of the room type | [optional] 
**room_name** | **str** | Name of the specific room. N/A means not applicable, and it is used if the transaction is not linked to a room. | [optional] 
**guest_name** | **str** | Name of the first guest of the reservation | [optional] 
**description** | **str** | Description of the transaction | [optional] 
**category** | **str** | Category of the transaction | [optional] 
**transaction_code** | **str** | Transaction identifier that can be used, or left blank | [optional] 
**notes** | **str** | If any special information needs to be added to the transaction, it will be in this field | [optional] 
**quantity** | **int** |  | [optional] 
**amount** | **float** | Consolidated amount on the transaction (Credit - Debit) | [optional] 
**currency** | **str** | Currency of the transaction | [optional] 
**user_name** | **str** | User responsible for creating the transaction | [optional] 
**transaction_type** | **str** | Consolidated transaction type | [optional] 
**transaction_category** | **str** | Transaction category | [optional] 
**item_category_name** | **str** | Item category name | [optional] 
**transaction_id** | **str** | Transaction identifier | [optional] 
**parent_transaction_id** | **str** | Parent transaction identifier. Parent transaction is a transaction to which this current transaction is strongly related to or derived from.&lt;br/&gt; Example: Parent transaction to a room rate tax is a room rate.&lt;br/&gt; This parent transaction ID will mostly be present on transactions that are taxes, fees and voids. It will not be present on room rates, items, payments and refunds. | [optional] 
**card_type** | **str** | Abbreviated name of credit card type | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_transactions_response_data_inner import GetTransactionsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponseDataInner from a JSON string
get_transactions_response_data_inner_instance = GetTransactionsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponseDataInner.to_json())

# convert the object into a dict
get_transactions_response_data_inner_dict = get_transactions_response_data_inner_instance.to_dict()
# create an instance of GetTransactionsResponseDataInner from a dict
get_transactions_response_data_inner_from_dict = GetTransactionsResponseDataInner.from_dict(get_transactions_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


