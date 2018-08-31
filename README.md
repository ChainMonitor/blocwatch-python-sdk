# blocwatch-v1
The premier crypto API for blockchain analysis

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: Alpha v.0.0.1
- Package version: 0.5.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.blocwatch.com/support](https://www.blocwatch.com/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import blocwatch_v1 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import blocwatch_v1
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import blocwatch_v1
from blocwatch_v1.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
blocwatch_v1.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = blocwatch_v1.BitcoinAddressesApi()
id = 'id_example' # str | id
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    # getAddress
    api_response = api_instance.get_address(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinAddressesApi->get_address: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.blocwatch.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BitcoinAddressesApi* | [**get_address**](docs/BitcoinAddressesApi.md#get_address) | **GET** /v1/bitcoin/addresses/{id} | getAddress
*BitcoinAddressesApi* | [**list_address_usages**](docs/BitcoinAddressesApi.md#list_address_usages) | **GET** /v1/bitcoin/addresses/{id}/usages | listAddressUsages
*BitcoinBlocksApi* | [**get_block**](docs/BitcoinBlocksApi.md#get_block) | **GET** /v1/bitcoin/blocks/{id} | getBlock
*BitcoinBlocksApi* | [**get_top_block**](docs/BitcoinBlocksApi.md#get_top_block) | **GET** /v1/bitcoin/blocks/top | getTopBlock
*BitcoinBlocksApi* | [**list_block_transactions**](docs/BitcoinBlocksApi.md#list_block_transactions) | **GET** /v1/bitcoin/blocks/{id}/transactions | listBlockTransactions
*BitcoinBlocksApi* | [**list_blocks**](docs/BitcoinBlocksApi.md#list_blocks) | **GET** /v1/bitcoin/blocks | listBlocks
*BitcoinTransactionIteratorsApi* | [**create_iterator**](docs/BitcoinTransactionIteratorsApi.md#create_iterator) | **POST** /v1/bitcoin/transactions/iterators | createIterator
*BitcoinTransactionIteratorsApi* | [**get_transactions**](docs/BitcoinTransactionIteratorsApi.md#get_transactions) | **GET** /v1/bitcoin/transactions/iterators | getTransactions
*BitcoinTransactionsApi* | [**get_transaction**](docs/BitcoinTransactionsApi.md#get_transaction) | **GET** /v1/bitcoin/transactions/{id} | getTransaction
*BitcoinTransactionsApi* | [**get_transaction_input**](docs/BitcoinTransactionsApi.md#get_transaction_input) | **GET** /v1/bitcoin/transactions/{id}/inputs/{index} | getTransactionInput
*BitcoinTransactionsApi* | [**get_transaction_output**](docs/BitcoinTransactionsApi.md#get_transaction_output) | **GET** /v1/bitcoin/transactions/{id}/outputs/{index} | getTransactionOutput
*BitcoinTransactionsApi* | [**list_transactions**](docs/BitcoinTransactionsApi.md#list_transactions) | **GET** /v1/bitcoin/transactions | listTransactions
*BitcoinTransactionsApi* | [**list_transactions_inputs**](docs/BitcoinTransactionsApi.md#list_transactions_inputs) | **GET** /v1/bitcoin/transactions/{id}/inputs | listTransactionsInputs
*BitcoinTransactionsApi* | [**list_transactions_outputs**](docs/BitcoinTransactionsApi.md#list_transactions_outputs) | **GET** /v1/bitcoin/transactions/{id}/outputs | listTransactionsOutputs
*BitcoinTransactionsApi* | [**search_transactions**](docs/BitcoinTransactionsApi.md#search_transactions) | **POST** /v1/bitcoin/transactions/search | searchTransactions


## Documentation For Models

 - [BitcoinAddress](docs/BitcoinAddress.md)
 - [BitcoinBlock](docs/BitcoinBlock.md)
 - [BitcoinCompareQuery](docs/BitcoinCompareQuery.md)
 - [BitcoinInput](docs/BitcoinInput.md)
 - [BitcoinOutput](docs/BitcoinOutput.md)
 - [BitcoinQuery](docs/BitcoinQuery.md)
 - [BitcoinSearchRequest](docs/BitcoinSearchRequest.md)
 - [BitcoinTransaction](docs/BitcoinTransaction.md)
 - [CreateIteratorRequest](docs/CreateIteratorRequest.md)
 - [CreateIteratorResponse](docs/CreateIteratorResponse.md)
 - [Details](docs/Details.md)
 - [GetAddressResponse](docs/GetAddressResponse.md)
 - [GetBlockResponse](docs/GetBlockResponse.md)
 - [GetTransactionInputResponse](docs/GetTransactionInputResponse.md)
 - [GetTransactionOutputResponse](docs/GetTransactionOutputResponse.md)
 - [GetTransactionResponse](docs/GetTransactionResponse.md)
 - [GetTransactionsResponse](docs/GetTransactionsResponse.md)
 - [GroupQuery](docs/GroupQuery.md)
 - [InputDetails](docs/InputDetails.md)
 - [ListAddressUsagesResponse](docs/ListAddressUsagesResponse.md)
 - [ListBlockTransactionsResponse](docs/ListBlockTransactionsResponse.md)
 - [ListBlocksResponse](docs/ListBlocksResponse.md)
 - [ListTransactionInputsResponse](docs/ListTransactionInputsResponse.md)
 - [ListTransactionOutputsResponse](docs/ListTransactionOutputsResponse.md)
 - [ListTransactionsResponse](docs/ListTransactionsResponse.md)
 - [OutputDetails](docs/OutputDetails.md)
 - [Page](docs/Page.md)
 - [Summary](docs/Summary.md)
 - [TimeWindow](docs/TimeWindow.md)
 - [Usage](docs/Usage.md)
 - [UsageIn](docs/UsageIn.md)
 - [UsageOut](docs/UsageOut.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api.blocwatch.com/oauth/authorize
- **Scopes**: N/A


## Author

support@blocwatch.com
