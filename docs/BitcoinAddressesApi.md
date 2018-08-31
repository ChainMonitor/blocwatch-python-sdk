# blocwatch_v1.BitcoinAddressesApi

All URIs are relative to *https://api.blocwatch.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](BitcoinAddressesApi.md#get_address) | **GET** /v1/bitcoin/addresses/{id} | getAddress
[**list_address_usages**](BitcoinAddressesApi.md#list_address_usages) | **GET** /v1/bitcoin/addresses/{id}/usages | listAddressUsages


# **get_address**
> GetAddressResponse get_address(id, include=include)

getAddress

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
api_instance = blocwatch_v1.BitcoinAddressesApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
include = ['basic'] # list[str] | include (optional) (default to basic)

try:
    # getAddress
    api_response = api_instance.get_address(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinAddressesApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **include** | [**list[str]**](str.md)| include | [optional] [default to basic]

### Return type

[**GetAddressResponse**](GetAddressResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_usages**
> ListAddressUsagesResponse list_address_usages(id, page_limit=page_limit, page_token=page_token)

listAddressUsages

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
api_instance = blocwatch_v1.BitcoinAddressesApi(blocwatch_v1.ApiClient(configuration))
id = 'id_example' # str | id
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # listAddressUsages
    api_response = api_instance.list_address_usages(id, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinAddressesApi->list_address_usages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **page_limit** | **int**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListAddressUsagesResponse**](ListAddressUsagesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

