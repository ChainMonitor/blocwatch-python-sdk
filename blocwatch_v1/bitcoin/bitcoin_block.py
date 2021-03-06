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

from blocwatch_v1.bitcoin.details import Details  # noqa: F401,E501
from blocwatch_v1.bitcoin.summary import Summary  # noqa: F401,E501


class BitcoinBlock(object):
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
        'details': 'Details',
        'hash': 'str',
        'height': 'int',
        'median_time': 'datetime',
        'miner_time': 'datetime',
        'name': 'str',
        'summary': 'Summary'
    }

    attribute_map = {
        'details': 'details',
        'hash': 'hash',
        'height': 'height',
        'median_time': 'medianTime',
        'miner_time': 'minerTime',
        'name': 'name',
        'summary': 'summary'
    }

    def __init__(self, details=None, hash=None, height=None, median_time=None, miner_time=None, name=None, summary=None):  # noqa: E501
        """BitcoinBlock - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._hash = None
        self._height = None
        self._median_time = None
        self._miner_time = None
        self._name = None
        self._summary = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if hash is not None:
            self.hash = hash
        if height is not None:
            self.height = height
        if median_time is not None:
            self.median_time = median_time
        if miner_time is not None:
            self.miner_time = miner_time
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary

    @property
    def details(self):
        """Gets the details of this BitcoinBlock.  # noqa: E501

        Detailed information from this block.  # noqa: E501

        :return: The details of this BitcoinBlock.  # noqa: E501
        :rtype: Details
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BitcoinBlock.

        Detailed information from this block.  # noqa: E501

        :param details: The details of this BitcoinBlock.  # noqa: E501
        :type: Details
        """

        self._details = details

    @property
    def hash(self):
        """Gets the hash of this BitcoinBlock.  # noqa: E501

        The unique hash that identifies this block.  # noqa: E501

        :return: The hash of this BitcoinBlock.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BitcoinBlock.

        The unique hash that identifies this block.  # noqa: E501

        :param hash: The hash of this BitcoinBlock.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def height(self):
        """Gets the height of this BitcoinBlock.  # noqa: E501

        The height (distance) of this block from the genesis block (block 0).  # noqa: E501

        :return: The height of this BitcoinBlock.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BitcoinBlock.

        The height (distance) of this block from the genesis block (block 0).  # noqa: E501

        :param height: The height of this BitcoinBlock.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def median_time(self):
        """Gets the median_time of this BitcoinBlock.  # noqa: E501

        The median time of this block.    <p> The median time is defined as the median of the time of the previous 11 mined blocks.  # noqa: E501

        :return: The median_time of this BitcoinBlock.  # noqa: E501
        :rtype: datetime
        """
        return self._median_time

    @median_time.setter
    def median_time(self, median_time):
        """Sets the median_time of this BitcoinBlock.

        The median time of this block.    <p> The median time is defined as the median of the time of the previous 11 mined blocks.  # noqa: E501

        :param median_time: The median_time of this BitcoinBlock.  # noqa: E501
        :type: datetime
        """

        self._median_time = median_time

    @property
    def miner_time(self):
        """Gets the miner_time of this BitcoinBlock.  # noqa: E501

        The time that the miner that mined this block attached to this block.  # noqa: E501

        :return: The miner_time of this BitcoinBlock.  # noqa: E501
        :rtype: datetime
        """
        return self._miner_time

    @miner_time.setter
    def miner_time(self, miner_time):
        """Sets the miner_time of this BitcoinBlock.

        The time that the miner that mined this block attached to this block.  # noqa: E501

        :param miner_time: The miner_time of this BitcoinBlock.  # noqa: E501
        :type: datetime
        """

        self._miner_time = miner_time

    @property
    def name(self):
        """Gets the name of this BitcoinBlock.  # noqa: E501


        :return: The name of this BitcoinBlock.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BitcoinBlock.


        :param name: The name of this BitcoinBlock.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def summary(self):
        """Gets the summary of this BitcoinBlock.  # noqa: E501

        Summary information for this block.  # noqa: E501

        :return: The summary of this BitcoinBlock.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this BitcoinBlock.

        Summary information for this block.  # noqa: E501

        :param summary: The summary of this BitcoinBlock.  # noqa: E501
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BitcoinBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
