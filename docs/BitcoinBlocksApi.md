# blocwatch_v1.BitcoinBlocksApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](BitcoinBlocksApi.md#get_block) | **GET** /v1/bitcoin/blocks/{id} | Get a single block by block hash.
[**get_top_block**](BitcoinBlocksApi.md#get_top_block) | **GET** /v1/bitcoin/blocks/top | Fetch the most recent accepted block.
[**list_block_transactions**](BitcoinBlocksApi.md#list_block_transactions) | **GET** /v1/bitcoin/blocks/{id}/transactions | List transactions within a single block.
[**list_blocks**](BitcoinBlocksApi.md#list_blocks) | **GET** /v1/bitcoin/blocks | List blocks matching given criteria.


# **get_block**
> GetBlockResponse get_block(id, include=include)

Get a single block by block hash.

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
api_instance = blocwatch_v1.BitcoinBlocksApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | The hash of the block to fetch.
include = ['basic'] # list[str] | Information to include with the block. (optional) (default to basic)

try:
    # Get a single block by block hash.
    api_response = api_instance.get_block(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinBlocksApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The hash of the block to fetch. | 
 **include** | [**list[str]**](str.md)| Information to include with the block. | [optional] [default to basic]

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_block**
> GetBlockResponse get_top_block(include=include)

Fetch the most recent accepted block.

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
api_instance = blocwatch_v1.BitcoinBlocksApi(blocwatch_v1.ApiClient(configuration))
include = ['basic'] # list[str] | Information to include with the block. (optional) (default to basic)

try:
    # Fetch the most recent accepted block.
    api_response = api_instance.get_top_block(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinBlocksApi->get_top_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Information to include with the block. | [optional] [default to basic]

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_transactions**
> ListBlockTransactionsResponse list_block_transactions(id, include=include, page_limit=page_limit, page_token=page_token)

List transactions within a single block.

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
api_instance = blocwatch_v1.BitcoinBlocksApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | Block-hash for which information should be returned.
include = ['basic'] # list[str] | Specify which information to include in returned transactions. (optional) (default to basic)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # List transactions within a single block.
    api_response = api_instance.list_block_transactions(id, include=include, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinBlocksApi->list_block_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Block-hash for which information should be returned. | 
 **include** | [**list[str]**](str.md)| Specify which information to include in returned transactions. | [optional] [default to basic]
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListBlockTransactionsResponse**](ListBlockTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocks**
> ListBlocksResponse list_blocks(confirmations_max=confirmations_max, confirmations_min=confirmations_min, height_max=height_max, height_min=height_min, ids=ids, include=include, page_limit=page_limit, page_token=page_token, time_max=time_max, time_min=time_min, time_type=time_type)

List blocks matching given criteria.

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
api_instance = blocwatch_v1.BitcoinBlocksApi(blocwatch_v1.ApiClient(configuration))
confirmations_max = 56 # int |  (optional)
confirmations_min = 56 # int |  (optional)
height_max = 56 # int |  (optional)
height_min = 56 # int |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
include = ['basic'] # list[str] | Specify which information to include in returned blocks. (optional) (default to basic)
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)
time_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
time_min = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
time_type = 'time_type_example' # str |  (optional)

try:
    # List blocks matching given criteria.
    api_response = api_instance.list_blocks(confirmations_max=confirmations_max, confirmations_min=confirmations_min, height_max=height_max, height_min=height_min, ids=ids, include=include, page_limit=page_limit, page_token=page_token, time_max=time_max, time_min=time_min, time_type=time_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinBlocksApi->list_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirmations_max** | **int**|  | [optional] 
 **confirmations_min** | **int**|  | [optional] 
 **height_max** | **int**|  | [optional] 
 **height_min** | **int**|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **include** | [**list[str]**](str.md)| Specify which information to include in returned blocks. | [optional] [default to basic]
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 
 **time_max** | **datetime**|  | [optional] 
 **time_min** | **datetime**|  | [optional] 
 **time_type** | **str**|  | [optional] 

### Return type

[**ListBlocksResponse**](ListBlocksResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

