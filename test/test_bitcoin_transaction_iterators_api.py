# coding: utf-8

"""
    Blocwatch REST API

    The premier crypto API for blockchain analysis  # noqa: E501

    OpenAPI spec version: Alpha v.0.0.1
    Contact: support@blocwatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import blocwatch_v1
from blocwatch_v1.api.bitcoin_transaction_iterators_api import BitcoinTransactionIteratorsApi  # noqa: E501
from blocwatch_v1.rest import ApiException


class TestBitcoinTransactionIteratorsApi(unittest.TestCase):
    """BitcoinTransactionIteratorsApi unit test stubs"""

    def setUp(self):
        self.api = blocwatch_v1.api.bitcoin_transaction_iterators_api.BitcoinTransactionIteratorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_iterator(self):
        """Test case for create_iterator

        createIterator  # noqa: E501
        """
        pass

    def test_get_transactions(self):
        """Test case for get_transactions

        getTransactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
