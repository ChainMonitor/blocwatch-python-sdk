# BitcoinInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_names** | **list[str]** | Bitcoin Addresses that are known to be sources for this transaction input. | [optional] 
**bitcoin_value** | **float** | The value of this input in BTC. | [optional] 
**coinbase_input** | **bool** |  | [optional] 
**details** | [**InputDetails**](InputDetails.md) | Details of this transaction input, if requested. | [optional] 
**input_index** | **int** | The position of this input within the transaction (e.g., ordinal in vin). | [optional] 
**median_time** | **datetime** | The medianTime of the block that included the transaction output that this input spends. | [optional] 
**miner_time** | **datetime** | The minerTime of the block that included the transaction output that this input spends. | [optional] 
**name** | **str** |  | [optional] 
**signatures** | **int** | Number of signatures provided for this input. | [optional] 
**transaction_name** | **str** | The name of the transaction that supplied this input value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


