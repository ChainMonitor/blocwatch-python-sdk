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

from blocwatch_v1.bitcoin.bitcoin_input import BitcoinInput  # noqa: F401,E501
from blocwatch_v1.bitcoin.bitcoin_transaction import BitcoinTransaction  # noqa: F401,E501
from blocwatch_v1.bitcoin.page import Page  # noqa: F401,E501


class ListTransactionInputsResponse(object):
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
        'inputs': 'list[BitcoinInput]',
        'page': 'Page',
        'transaction': 'BitcoinTransaction'
    }

    attribute_map = {
        'inputs': 'inputs',
        'page': 'page',
        'transaction': 'transaction'
    }

    def __init__(self, inputs=None, page=None, transaction=None):  # noqa: E501
        """ListTransactionInputsResponse - a model defined in Swagger"""  # noqa: E501

        self._inputs = None
        self._page = None
        self._transaction = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if page is not None:
            self.page = page
        if transaction is not None:
            self.transaction = transaction

    @property
    def inputs(self):
        """Gets the inputs of this ListTransactionInputsResponse.  # noqa: E501

        The requested transaction inputs.  # noqa: E501

        :return: The inputs of this ListTransactionInputsResponse.  # noqa: E501
        :rtype: list[BitcoinInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ListTransactionInputsResponse.

        The requested transaction inputs.  # noqa: E501

        :param inputs: The inputs of this ListTransactionInputsResponse.  # noqa: E501
        :type: list[BitcoinInput]
        """

        self._inputs = inputs

    @property
    def page(self):
        """Gets the page of this ListTransactionInputsResponse.  # noqa: E501


        :return: The page of this ListTransactionInputsResponse.  # noqa: E501
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTransactionInputsResponse.


        :param page: The page of this ListTransactionInputsResponse.  # noqa: E501
        :type: Page
        """

        self._page = page

    @property
    def transaction(self):
        """Gets the transaction of this ListTransactionInputsResponse.  # noqa: E501

        The transaction containing the listed inputs.  # noqa: E501

        :return: The transaction of this ListTransactionInputsResponse.  # noqa: E501
        :rtype: BitcoinTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ListTransactionInputsResponse.

        The transaction containing the listed inputs.  # noqa: E501

        :param transaction: The transaction of this ListTransactionInputsResponse.  # noqa: E501
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTransactionInputsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
