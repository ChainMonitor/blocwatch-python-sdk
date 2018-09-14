# coding: utf-8

"""
    Blocwatch REST API

    The premier API for blockchain analysis  # noqa: E501

    OpenAPI spec version: v1.0.0
    Contact: support@blocwatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

import blocwatch_v1.bitcoin.bitcoin_input  # noqa: F401,E501
import blocwatch_v1.bitcoin.bitcoin_transaction  # noqa: F401,E501


class GetTransactionInputResponse(object):
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
        'input': 'BitcoinInput',
        'transaction': 'BitcoinTransaction'
    }

    attribute_map = {
        'input': 'input',
        'transaction': 'transaction'
    }

    def __init__(self, input=None, transaction=None):  # noqa: E501
        """GetTransactionInputResponse - a model defined in Swagger"""  # noqa: E501

        self._input = None
        self._transaction = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if transaction is not None:
            self.transaction = transaction

    @property
    def input(self):
        """Gets the input of this GetTransactionInputResponse.  # noqa: E501

        The requested transaction input.  # noqa: E501

        :return: The input of this GetTransactionInputResponse.  # noqa: E501
        :rtype: BitcoinInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this GetTransactionInputResponse.

        The requested transaction input.  # noqa: E501

        :param input: The input of this GetTransactionInputResponse.  # noqa: E501
        :type: BitcoinInput
        """

        self._input = input

    @property
    def transaction(self):
        """Gets the transaction of this GetTransactionInputResponse.  # noqa: E501

        The transaction containing this transaction input.  # noqa: E501

        :return: The transaction of this GetTransactionInputResponse.  # noqa: E501
        :rtype: BitcoinTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this GetTransactionInputResponse.

        The transaction containing this transaction input.  # noqa: E501

        :param transaction: The transaction of this GetTransactionInputResponse.  # noqa: E501
        :type: BitcoinTransaction
        """

        self._transaction = transaction

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
        if issubclass(GetTransactionInputResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetTransactionInputResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
