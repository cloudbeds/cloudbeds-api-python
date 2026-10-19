# CheckItemTypeEnum

Line item kind — also the discriminator that selects the concrete shape of the `details` block on the same item. Currently only PRODUCT is accepted (ordinary POS items: food / beverage / retail), and `details` is a ProductDetailsSchema. BOOKABLE_RESOURCE will be reintroduced once the bookable-resource service exposes the synchronous create-reservation RPC postCheck needs to route those lines.

## Enum

* `PRODUCT` (value: `'PRODUCT'`)

* `UNKNOWN_DEFAULT_OPEN_API` (value: `'unknown_default_open_api'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


