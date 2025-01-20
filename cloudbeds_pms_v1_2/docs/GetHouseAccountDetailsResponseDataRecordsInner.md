# GetHouseAccountDetailsResponseDataRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**transaction_id** | **str** | Transaction ID | [optional] 
**user_name** | **str** | User name | [optional] 
**description** | **str** | Record description | [optional] 
**notes** | **str** | Record notes | [optional] 
**quantity** | **str** | Quantity of items (for product type record) | [optional] 
**debit** | **str** | Debit amount (non formatted) | [optional] 
**credit** | **str** | Credit amount (non formatted) | [optional] 
**debit_formatter** | **str** | Debit amount (formatted) | [optional] 
**credit_formatted** | **str** | Credit amount (formatted) | [optional] 
**currency** | **str** | Currency string | [optional] 
**transaction_code** | **str** | Transaction code | [optional] 
**parent_transaction_id** | **str** | Parent transaction identifier. Parent transaction is a transaction to which this current transaction is strongly related to or derived from.&lt;br/&gt; Example: Parent transaction to a room rate tax is a room rate.&lt;br/&gt; This parent transaction ID will mostly be present on transactions that are taxes, fees and voids. It will not be present on room rates, items, payments and refunds. | [optional] 
**transaction_date** | **date** | Transaction date | [optional] 
**transaction_date_time** | **datetime** | Transaction date and time | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_house_account_details_response_data_records_inner import GetHouseAccountDetailsResponseDataRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHouseAccountDetailsResponseDataRecordsInner from a JSON string
get_house_account_details_response_data_records_inner_instance = GetHouseAccountDetailsResponseDataRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetHouseAccountDetailsResponseDataRecordsInner.to_json())

# convert the object into a dict
get_house_account_details_response_data_records_inner_dict = get_house_account_details_response_data_records_inner_instance.to_dict()
# create an instance of GetHouseAccountDetailsResponseDataRecordsInner from a dict
get_house_account_details_response_data_records_inner_from_dict = GetHouseAccountDetailsResponseDataRecordsInner.from_dict(get_house_account_details_response_data_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


