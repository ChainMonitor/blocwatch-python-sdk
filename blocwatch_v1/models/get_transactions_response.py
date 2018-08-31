# coding: utf-8

"""
    Blocwatch REST API

    The premier crypto API for blockchain analysis  # noqa: E501

    OpenAPI spec version: Alpha v.0.0.1
    Contact: support@blocwatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from blocwatch_v1.models.bitcoin_transaction import BitcoinTransaction  # noqa: F401,E501


class GetTransactionsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'iterator_token': 'str',
        'transactions': 'list[BitcoinTransaction]'
    }

    attribute_map = {
        'iterator_token': 'iteratorToken',
        'transactions': 'transactions'
    }

    def __init__(self, iterator_token=None, transactions=None):  # noqa: E501
        """GetTransactionsResponse - a model defined in Swagger"""  # noqa: E501

        self._iterator_token = None
        self._transactions = None
        self.discriminator = None

        if iterator_token is not None:
            self.iterator_token = iterator_token
        if transactions is not None:
            self.transactions = transactions

    @property
    def iterator_token(self):
        """Gets the iterator_token of this GetTransactionsResponse.  # noqa: E501


        :return: The iterator_token of this GetTransactionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._iterator_token

    @iterator_token.setter
    def iterator_token(self, iterator_token):
        """Sets the iterator_token of this GetTransactionsResponse.


        :param iterator_token: The iterator_token of this GetTransactionsResponse.  # noqa: E501
        :type: str
        """

        self._iterator_token = iterator_token

    @property
    def transactions(self):
        """Gets the transactions of this GetTransactionsResponse.  # noqa: E501


        :return: The transactions of this GetTransactionsResponse.  # noqa: E501
        :rtype: list[BitcoinTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this GetTransactionsResponse.


        :param transactions: The transactions of this GetTransactionsResponse.  # noqa: E501
        :type: list[BitcoinTransaction]
        """

        self._transactions = transactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
