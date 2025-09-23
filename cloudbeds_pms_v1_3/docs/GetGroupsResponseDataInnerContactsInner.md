# GetGroupsResponseDataInnerContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for a contact | [optional] 
**group_profile_id** | **str** | The group profile ID this contact belongs to | [optional] 
**primary** | **bool** | Whether this is the primary contact | [optional] 
**anonymized** | **bool** | Whether the contact is anonymized | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**role** | **str** | Contact role | [optional] 
**status** | **str** | Contact status | [optional] 
**created_at** | **datetime** | Contact creation time | [optional] 
**updated_at** | **datetime** | Contact last update time | [optional] 
**emails** | [**List[GetGroupsResponseDataInnerContactsInnerEmailsInner]**](GetGroupsResponseDataInnerContactsInnerEmailsInner.md) | Contact email addresses | [optional] 
**phones** | [**List[GetGroupsResponseDataInnerContactsInnerPhonesInner]**](GetGroupsResponseDataInnerContactsInnerPhonesInner.md) | Contact phone numbers | [optional] 
**is_billing_recipient** | **bool** | Whether this contact is a billing recipient | [optional] 
**tax_id_number** | **str** | Contact tax ID number | [optional] 
**tax_document_type** | **str** | Contact tax document type | [optional] 
**legal_name** | **str** | Contact legal name | [optional] 
**address_1** | **str** | Contact address line 1 | [optional] 
**address_2** | **str** | Contact address line 2 | [optional] 
**city** | **str** | Contact city | [optional] 
**state** | **str** | Contact state | [optional] 
**country_code** | **str** | Contact country code | [optional] 
**zip** | **str** | Contact zip code | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_groups_response_data_inner_contacts_inner import GetGroupsResponseDataInnerContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsResponseDataInnerContactsInner from a JSON string
get_groups_response_data_inner_contacts_inner_instance = GetGroupsResponseDataInnerContactsInner.from_json(json)
# print the JSON string representation of the object
print(GetGroupsResponseDataInnerContactsInner.to_json())

# convert the object into a dict
get_groups_response_data_inner_contacts_inner_dict = get_groups_response_data_inner_contacts_inner_instance.to_dict()
# create an instance of GetGroupsResponseDataInnerContactsInner from a dict
get_groups_response_data_inner_contacts_inner_from_dict = GetGroupsResponseDataInnerContactsInner.from_dict(get_groups_response_data_inner_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


