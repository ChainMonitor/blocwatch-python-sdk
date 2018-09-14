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

import blocwatch_v1.bitcoin.summary  # noqa: F401,E501


class BitcoinAddress(object):
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
        'address': 'str',
        'name': 'str',
        'summary': 'Summary'
    }

    attribute_map = {
        'address': 'address',
        'name': 'name',
        'summary': 'summary'
    }

    def __init__(self, address=None, name=None, summary=None):  # noqa: E501
        """BitcoinAddress - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._name = None
        self._summary = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary

    @property
    def address(self):
        """Gets the address of this BitcoinAddress.  # noqa: E501

        Bitcoin Base58-Check or bech32 encoded address.  # noqa: E501

        :return: The address of this BitcoinAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BitcoinAddress.

        Bitcoin Base58-Check or bech32 encoded address.  # noqa: E501

        :param address: The address of this BitcoinAddress.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def name(self):
        """Gets the name of this BitcoinAddress.  # noqa: E501


        :return: The name of this BitcoinAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BitcoinAddress.


        :param name: The name of this BitcoinAddress.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def summary(self):
        """Gets the summary of this BitcoinAddress.  # noqa: E501

        Summary information about this Bitcoin address.  # noqa: E501

        :return: The summary of this BitcoinAddress.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this BitcoinAddress.

        Summary information about this Bitcoin address.  # noqa: E501

        :param summary: The summary of this BitcoinAddress.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

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
        if issubclass(BitcoinAddress, dict):
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
        if not isinstance(other, BitcoinAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
