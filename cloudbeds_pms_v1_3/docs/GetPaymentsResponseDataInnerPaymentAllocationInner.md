# GetPaymentsResponseDataInnerPaymentAllocationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | ² Type of item described in allocation | [optional] 
**reference** | **str** | ² Reference of item described in allocation | [optional] 
**name** | **str** | ² Name of item described in allocation | [optional] 
**amount** | **float** | ² Amount of allocated of payment total | [optional] 
**taxes** | **List[str]** | ² Taxes of allocated payment. Values are an array numeric of taxes IDs | [optional] 
**fees** | **List[str]** | ² Fees of allocated payment. Values are an array numeric of fees IDs | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_payments_response_data_inner_payment_allocation_inner import GetPaymentsResponseDataInnerPaymentAllocationInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsResponseDataInnerPaymentAllocationInner from a JSON string
get_payments_response_data_inner_payment_allocation_inner_instance = GetPaymentsResponseDataInnerPaymentAllocationInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsResponseDataInnerPaymentAllocationInner.to_json())

# convert the object into a dict
get_payments_response_data_inner_payment_allocation_inner_dict = get_payments_response_data_inner_payment_allocation_inner_instance.to_dict()
# create an instance of GetPaymentsResponseDataInnerPaymentAllocationInner from a dict
get_payments_response_data_inner_payment_allocation_inner_from_dict = GetPaymentsResponseDataInnerPaymentAllocationInner.from_dict(get_payments_response_data_inner_payment_allocation_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


