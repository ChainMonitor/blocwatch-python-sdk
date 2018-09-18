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

import blocwatch_v1.bitcoin.bitcoin_query  # noqa: F401,E501


class CreateIteratorRequest(object):
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
        'bitcoin_time_type': 'str',
        'from_block_height': 'int',
        'from_timestamp': 'datetime',
        'iterator_type': 'str',
        'query': 'BitcoinQuery'
    }

    attribute_map = {
        'bitcoin_time_type': 'bitcoinTimeType',
        'from_block_height': 'fromBlockHeight',
        'from_timestamp': 'fromTimestamp',
        'iterator_type': 'iteratorType',
        'query': 'query'
    }

    def __init__(self, bitcoin_time_type=None, from_block_height=None, from_timestamp=None, iterator_type=None, query=None):  # noqa: E501
        """CreateIteratorRequest - a model defined in Swagger"""  # noqa: E501

        self._bitcoin_time_type = None
        self._from_block_height = None
        self._from_timestamp = None
        self._iterator_type = None
        self._query = None
        self.discriminator = None

        if bitcoin_time_type is not None:
            self.bitcoin_time_type = bitcoin_time_type
        if from_block_height is not None:
            self.from_block_height = from_block_height
        if from_timestamp is not None:
            self.from_timestamp = from_timestamp
        if iterator_type is not None:
            self.iterator_type = iterator_type
        if query is not None:
            self.query = query

    @property
    def bitcoin_time_type(self):
        """Gets the bitcoin_time_type of this CreateIteratorRequest.  # noqa: E501


        :return: The bitcoin_time_type of this CreateIteratorRequest.  # noqa: E501
        :rtype: str
        """
        return self._bitcoin_time_type

    @bitcoin_time_type.setter
    def bitcoin_time_type(self, bitcoin_time_type):
        """Sets the bitcoin_time_type of this CreateIteratorRequest.


        :param bitcoin_time_type: The bitcoin_time_type of this CreateIteratorRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MINER", "MEDIAN"]  # noqa: E501
        if bitcoin_time_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bitcoin_time_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bitcoin_time_type, allowed_values)
            )

        self._bitcoin_time_type = bitcoin_time_type

    @property
    def from_block_height(self):
        """Gets the from_block_height of this CreateIteratorRequest.  # noqa: E501


        :return: The from_block_height of this CreateIteratorRequest.  # noqa: E501
        :rtype: int
        """
        return self._from_block_height

    @from_block_height.setter
    def from_block_height(self, from_block_height):
        """Sets the from_block_height of this CreateIteratorRequest.


        :param from_block_height: The from_block_height of this CreateIteratorRequest.  # noqa: E501
        :type: int
        """

        self._from_block_height = from_block_height

    @property
    def from_timestamp(self):
        """Gets the from_timestamp of this CreateIteratorRequest.  # noqa: E501


        :return: The from_timestamp of this CreateIteratorRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._from_timestamp

    @from_timestamp.setter
    def from_timestamp(self, from_timestamp):
        """Sets the from_timestamp of this CreateIteratorRequest.


        :param from_timestamp: The from_timestamp of this CreateIteratorRequest.  # noqa: E501
        :type: datetime
        """

        self._from_timestamp = from_timestamp

    @property
    def iterator_type(self):
        """Gets the iterator_type of this CreateIteratorRequest.  # noqa: E501


        :return: The iterator_type of this CreateIteratorRequest.  # noqa: E501
        :rtype: str
        """
        return self._iterator_type

    @iterator_type.setter
    def iterator_type(self, iterator_type):
        """Sets the iterator_type of this CreateIteratorRequest.


        :param iterator_type: The iterator_type of this CreateIteratorRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM_TIMESTAMP", "FROM_BLOCK_HEIGHT", "FROM_BEGINNING", "FROM_CHAIN_TIP"]  # noqa: E501
        if iterator_type not in allowed_values:
            raise ValueError(
                "Invalid value for `iterator_type` ({0}), must be one of {1}"  # noqa: E501
                .format(iterator_type, allowed_values)
            )

        self._iterator_type = iterator_type

    @property
    def query(self):
        """Gets the query of this CreateIteratorRequest.  # noqa: E501


        :return: The query of this CreateIteratorRequest.  # noqa: E501
        :rtype: BitcoinQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateIteratorRequest.


        :param query: The query of this CreateIteratorRequest.  # noqa: E501
        :type: BitcoinQuery
        """

        self._query = query

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
        if issubclass(CreateIteratorRequest, dict):
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
        if not isinstance(other, CreateIteratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
