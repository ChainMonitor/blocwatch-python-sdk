# blocwatch_v1.BitcoinTransactionIteratorsApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iterator**](BitcoinTransactionIteratorsApi.md#create_iterator) | **POST** /v1/bitcoin/transactions/iterators | 
[**get_transactions**](BitcoinTransactionIteratorsApi.md#get_transactions) | **GET** /v1/bitcoin/transactions/iterators | 


# **create_iterator**
> CreateIteratorResponse create_iterator(request, include=include)



### Example
```python
from __future__ import print_function
import time
import blocwatch_v1
from blocwatch_v1.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = blocwatch_v1.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = blocwatch_v1.BitcoinTransactionIteratorsApi(blocwatch_v1.ApiClient(configuration))
request = blocwatch_v1.CreateIteratorRequest() # blocwatch_v1.bitcoin.CreateIteratorRequest | request
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    api_response = api_instance.create_iterator(request, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionIteratorsApi->create_iterator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**blocwatch_v1.bitcoin.CreateIteratorRequest**](CreateIteratorRequest.md)| request | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]

### Return type

[**CreateIteratorResponse**](CreateIteratorResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> GetTransactionsResponse get_transactions(iterator_token, batch_size=batch_size)



### Example
```python
from __future__ import print_function
import time
import blocwatch_v1
from blocwatch_v1.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = blocwatch_v1.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = blocwatch_v1.BitcoinTransactionIteratorsApi(blocwatch_v1.ApiClient(configuration))
iterator_token = 'iterator_token_example' # str | iteratorToken
batch_size = 56 # int | batchSize (optional)

try:
    api_response = api_instance.get_transactions(iterator_token, batch_size=batch_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionIteratorsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iterator_token** | **str**| iteratorToken | 
 **batch_size** | **int**| batchSize | [optional] 

### Return type

[**GetTransactionsResponse**](GetTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

