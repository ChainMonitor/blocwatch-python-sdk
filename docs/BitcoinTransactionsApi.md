# blocwatch_v1.BitcoinTransactionsApi

All URIs are relative to *https://api.blocwatch.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction**](BitcoinTransactionsApi.md#get_transaction) | **GET** /v1/bitcoin/transactions/{id} | getTransaction
[**get_transaction_input**](BitcoinTransactionsApi.md#get_transaction_input) | **GET** /v1/bitcoin/transactions/{id}/inputs/{index} | getTransactionInput
[**get_transaction_output**](BitcoinTransactionsApi.md#get_transaction_output) | **GET** /v1/bitcoin/transactions/{id}/outputs/{index} | getTransactionOutput
[**list_transactions**](BitcoinTransactionsApi.md#list_transactions) | **GET** /v1/bitcoin/transactions | listTransactions
[**list_transactions_inputs**](BitcoinTransactionsApi.md#list_transactions_inputs) | **GET** /v1/bitcoin/transactions/{id}/inputs | listTransactionsInputs
[**list_transactions_outputs**](BitcoinTransactionsApi.md#list_transactions_outputs) | **GET** /v1/bitcoin/transactions/{id}/outputs | listTransactionsOutputs
[**search_transactions**](BitcoinTransactionsApi.md#search_transactions) | **POST** /v1/bitcoin/transactions/search | searchTransactions


# **get_transaction**
> GetTransactionResponse get_transaction(id, include=include)

getTransaction

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    # getTransaction
    api_response = api_instance.get_transaction(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_input**
> GetTransactionInputResponse get_transaction_input(id, index, include=include)

getTransactionInput

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
index = 56 # int | index
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    # getTransactionInput
    api_response = api_instance.get_transaction_input(id, index, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->get_transaction_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **index** | **int**| index | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]

### Return type

[**GetTransactionInputResponse**](GetTransactionInputResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_output**
> GetTransactionOutputResponse get_transaction_output(id, index, include=include)

getTransactionOutput

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
index = 56 # int | index
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    # getTransactionOutput
    api_response = api_instance.get_transaction_output(id, index, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->get_transaction_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **index** | **int**| index | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]

### Return type

[**GetTransactionOutputResponse**](GetTransactionOutputResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> ListTransactionsResponse list_transactions(confirmations_max=confirmations_max, confirmations_min=confirmations_min, height_max=height_max, height_min=height_min, ids=ids, include=include, inputs_max=inputs_max, inputs_min=inputs_min, max_time=max_time, min_time=min_time, outputs_max=outputs_max, outputs_min=outputs_min, page_limit=page_limit, page_token=page_token, payees=payees, payers=payers, value_max=value_max, value_min=value_min)

listTransactions

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
confirmations_max = 56 # int |  (optional)
confirmations_min = 56 # int |  (optional)
height_max = 56 # int |  (optional)
height_min = 56 # int |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
include = ['basic'] # list[str] | include (optional) (default to basic)
inputs_max = 56 # int |  (optional)
inputs_min = 56 # int |  (optional)
max_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
outputs_max = 56 # int |  (optional)
outputs_min = 56 # int |  (optional)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)
payees = ['payees_example'] # list[str] |  (optional)
payers = ['payers_example'] # list[str] |  (optional)
value_max = 1.2 # float |  (optional)
value_min = 1.2 # float |  (optional)

try:
    # listTransactions
    api_response = api_instance.list_transactions(confirmations_max=confirmations_max, confirmations_min=confirmations_min, height_max=height_max, height_min=height_min, ids=ids, include=include, inputs_max=inputs_max, inputs_min=inputs_min, max_time=max_time, min_time=min_time, outputs_max=outputs_max, outputs_min=outputs_min, page_limit=page_limit, page_token=page_token, payees=payees, payers=payers, value_max=value_max, value_min=value_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->list_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirmations_max** | **int**|  | [optional] 
 **confirmations_min** | **int**|  | [optional] 
 **height_max** | **int**|  | [optional] 
 **height_min** | **int**|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]
 **inputs_max** | **int**|  | [optional] 
 **inputs_min** | **int**|  | [optional] 
 **max_time** | **datetime**|  | [optional] 
 **min_time** | **datetime**|  | [optional] 
 **outputs_max** | **int**|  | [optional] 
 **outputs_min** | **int**|  | [optional] 
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 
 **payees** | [**list[str]**](str.md)|  | [optional] 
 **payers** | [**list[str]**](str.md)|  | [optional] 
 **value_max** | **float**|  | [optional] 
 **value_min** | **float**|  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions_inputs**
> ListTransactionInputsResponse list_transactions_inputs(id, include=include, page_limit=page_limit, page_token=page_token)

listTransactionsInputs

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
include = ['basic'] # list[str] | include (optional) (default to basic)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # listTransactionsInputs
    api_response = api_instance.list_transactions_inputs(id, include=include, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->list_transactions_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListTransactionInputsResponse**](ListTransactionInputsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions_outputs**
> ListTransactionOutputsResponse list_transactions_outputs(id, include=include, page_limit=page_limit, page_token=page_token)

listTransactionsOutputs

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
include = ['basic'] # list[str] | include (optional) (default to basic)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # listTransactionsOutputs
    api_response = api_instance.list_transactions_outputs(id, include=include, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->list_transactions_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListTransactionOutputsResponse**](ListTransactionOutputsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> ListTransactionsResponse search_transactions(search_request, include=include, page_limit=page_limit, page_token=page_token)

searchTransactions

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
api_instance = blocwatch_v1.BitcoinTransactionsApi(blocwatch_v1.ApiClient(configuration))
search_request = blocwatch_v1.BitcoinSearchRequest() # BitcoinSearchRequest | searchRequest
include = ['basic'] # list[str] | include (optional) (default to basic)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # searchTransactions
    api_response = api_instance.search_transactions(search_request, include=include, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinTransactionsApi->search_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**BitcoinSearchRequest**](BitcoinSearchRequest.md)| searchRequest | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

