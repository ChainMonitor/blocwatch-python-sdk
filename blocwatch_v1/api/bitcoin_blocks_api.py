# coding: utf-8

"""
    Blocwatch REST API

    The premier API for blockchain analysis  # noqa: E501

    OpenAPI spec version: v1.0.0
    Contact: support@blocwatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from blocwatch_v1.api_client import ApiClient


class BitcoinBlocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_block(self, id, **kwargs):  # noqa: E501
        """Get a single block by block hash.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The hash of the block to fetch. (required)
        :param list[str] include: Information to include with the block.
        :return: GetBlockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_block_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_block_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a single block by block hash.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The hash of the block to fetch. (required)
        :param list[str] include: Information to include with the block.
        :return: GetBlockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_block`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/bitcoin/blocks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetBlockResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_top_block(self, **kwargs):  # noqa: E501
        """Fetch the most recent accepted block.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_top_block(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] include: Information to include with the block.
        :return: GetBlockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_top_block_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_top_block_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_top_block_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch the most recent accepted block.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_top_block_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] include: Information to include with the block.
        :return: GetBlockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_top_block" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/bitcoin/blocks/top', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetBlockResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_block_transactions(self, id, **kwargs):  # noqa: E501
        """List transactions within a single block.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_transactions(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Block-hash for which information should be returned. (required)
        :param list[str] include: Specify which information to include in returned transactions.
        :param int page_limit:
        :param str page_token:
        :return: ListBlockTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_block_transactions_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_block_transactions_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_block_transactions_with_http_info(self, id, **kwargs):  # noqa: E501
        """List transactions within a single block.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_transactions_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Block-hash for which information should be returned. (required)
        :param list[str] include: Specify which information to include in returned transactions.
        :param int page_limit:
        :param str page_token:
        :return: ListBlockTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include', 'page_limit', 'page_token']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_block_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_block_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'multi'  # noqa: E501
        if 'page_limit' in params:
            query_params.append(('pageLimit', params['page_limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/bitcoin/blocks/{id}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListBlockTransactionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_blocks(self, **kwargs):  # noqa: E501
        """List blocks matching given criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_blocks(async=True)
        >>> result = thread.get()

        :param async bool
        :param int confirmations_max:
        :param int confirmations_min:
        :param int height_max:
        :param int height_min:
        :param list[str] ids:
        :param list[str] include: Specify which information to include in returned blocks.
        :param int page_limit:
        :param str page_token:
        :param datetime time_max:
        :param datetime time_min:
        :param str time_type:
        :return: ListBlocksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_blocks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_blocks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_blocks_with_http_info(self, **kwargs):  # noqa: E501
        """List blocks matching given criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_blocks_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int confirmations_max:
        :param int confirmations_min:
        :param int height_max:
        :param int height_min:
        :param list[str] ids:
        :param list[str] include: Specify which information to include in returned blocks.
        :param int page_limit:
        :param str page_token:
        :param datetime time_max:
        :param datetime time_min:
        :param str time_type:
        :return: ListBlocksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['confirmations_max', 'confirmations_min', 'height_max', 'height_min', 'ids', 'include', 'page_limit', 'page_token', 'time_max', 'time_min', 'time_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_blocks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'confirmations_max' in params:
            query_params.append(('confirmationsMax', params['confirmations_max']))  # noqa: E501
        if 'confirmations_min' in params:
            query_params.append(('confirmationsMin', params['confirmations_min']))  # noqa: E501
        if 'height_max' in params:
            query_params.append(('heightMax', params['height_max']))  # noqa: E501
        if 'height_min' in params:
            query_params.append(('heightMin', params['height_min']))  # noqa: E501
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
            collection_formats['include'] = 'multi'  # noqa: E501
        if 'page_limit' in params:
            query_params.append(('pageLimit', params['page_limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'time_max' in params:
            query_params.append(('timeMax', params['time_max']))  # noqa: E501
        if 'time_min' in params:
            query_params.append(('timeMin', params['time_min']))  # noqa: E501
        if 'time_type' in params:
            query_params.append(('timeType', params['time_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/bitcoin/blocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListBlocksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
