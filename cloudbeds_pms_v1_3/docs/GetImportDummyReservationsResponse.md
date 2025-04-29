# GetImportDummyReservationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | **List[str]** | Reservations details | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_import_dummy_reservations_response import GetImportDummyReservationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetImportDummyReservationsResponse from a JSON string
get_import_dummy_reservations_response_instance = GetImportDummyReservationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetImportDummyReservationsResponse.to_json())

# convert the object into a dict
get_import_dummy_reservations_response_dict = get_import_dummy_reservations_response_instance.to_dict()
# create an instance of GetImportDummyReservationsResponse from a dict
get_import_dummy_reservations_response_from_dict = GetImportDummyReservationsResponse.from_dict(get_import_dummy_reservations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


