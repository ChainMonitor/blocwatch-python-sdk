# blocwatch_v1.BitcoinAddressesApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](BitcoinAddressesApi.md#get_address) | **GET** /v1/bitcoin/addresses/{id} | Fetch details about a single address.
[**list_address_usages**](BitcoinAddressesApi.md#list_address_usages) | **GET** /v1/bitcoin/addresses/{id}/usages | List usages for a single address.


# **get_address**
> GetAddressResponse get_address(id, include=include)

Fetch details about a single address.

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
id = 'id_example' # str | The address for which details should be fetched.
include = ['basic'] # list[str] | Specify information to include with the address. (optional) (default to basic)

try:
    # Fetch details about a single address.
    api_response = api_instance.get_address(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinAddressesApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The address for which details should be fetched. | 
 **include** | [**list[str]**](str.md)| Specify information to include with the address. | [optional] [default to basic]

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

List usages for a single address.

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
id = 'id_example' # str | The address for which usages should be fetched.
page_limit = 56 # int |  (optional)
page_token = 'page_token_example' # str |  (optional)

try:
    # List usages for a single address.
    api_response = api_instance.list_address_usages(id, page_limit=page_limit, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinAddressesApi->list_address_usages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The address for which usages should be fetched. | 
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

