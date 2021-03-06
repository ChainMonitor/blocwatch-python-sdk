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

from blocwatch_v1.bitcoin.input_details import InputDetails  # noqa: F401,E501


class BitcoinInput(object):
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
        'address_names': 'list[str]',
        'bitcoin_value': 'float',
        'coinbase_input': 'bool',
        'details': 'InputDetails',
        'input_index': 'int',
        'median_time': 'datetime',
        'miner_time': 'datetime',
        'name': 'str',
        'signatures': 'int',
        'transaction_name': 'str'
    }

    attribute_map = {
        'address_names': 'addressNames',
        'bitcoin_value': 'bitcoinValue',
        'coinbase_input': 'coinbaseInput',
        'details': 'details',
        'input_index': 'inputIndex',
        'median_time': 'medianTime',
        'miner_time': 'minerTime',
        'name': 'name',
        'signatures': 'signatures',
        'transaction_name': 'transactionName'
    }

    def __init__(self, address_names=None, bitcoin_value=None, coinbase_input=None, details=None, input_index=None, median_time=None, miner_time=None, name=None, signatures=None, transaction_name=None):  # noqa: E501
        """BitcoinInput - a model defined in Swagger"""  # noqa: E501

        self._address_names = None
        self._bitcoin_value = None
        self._coinbase_input = None
        self._details = None
        self._input_index = None
        self._median_time = None
        self._miner_time = None
        self._name = None
        self._signatures = None
        self._transaction_name = None
        self.discriminator = None

        if address_names is not None:
            self.address_names = address_names
        if bitcoin_value is not None:
            self.bitcoin_value = bitcoin_value
        if coinbase_input is not None:
            self.coinbase_input = coinbase_input
        if details is not None:
            self.details = details
        if input_index is not None:
            self.input_index = input_index
        if median_time is not None:
            self.median_time = median_time
        if miner_time is not None:
            self.miner_time = miner_time
        if name is not None:
            self.name = name
        if signatures is not None:
            self.signatures = signatures
        if transaction_name is not None:
            self.transaction_name = transaction_name

    @property
    def address_names(self):
        """Gets the address_names of this BitcoinInput.  # noqa: E501

        Bitcoin Addresses that are known to be sources for this transaction input.  # noqa: E501

        :return: The address_names of this BitcoinInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_names

    @address_names.setter
    def address_names(self, address_names):
        """Sets the address_names of this BitcoinInput.

        Bitcoin Addresses that are known to be sources for this transaction input.  # noqa: E501

        :param address_names: The address_names of this BitcoinInput.  # noqa: E501
        :type: list[str]
        """

        self._address_names = address_names

    @property
    def bitcoin_value(self):
        """Gets the bitcoin_value of this BitcoinInput.  # noqa: E501

        The value of this input in BTC.  # noqa: E501

        :return: The bitcoin_value of this BitcoinInput.  # noqa: E501
        :rtype: float
        """
        return self._bitcoin_value

    @bitcoin_value.setter
    def bitcoin_value(self, bitcoin_value):
        """Sets the bitcoin_value of this BitcoinInput.

        The value of this input in BTC.  # noqa: E501

        :param bitcoin_value: The bitcoin_value of this BitcoinInput.  # noqa: E501
        :type: float
        """

        self._bitcoin_value = bitcoin_value

    @property
    def coinbase_input(self):
        """Gets the coinbase_input of this BitcoinInput.  # noqa: E501


        :return: The coinbase_input of this BitcoinInput.  # noqa: E501
        :rtype: bool
        """
        return self._coinbase_input

    @coinbase_input.setter
    def coinbase_input(self, coinbase_input):
        """Sets the coinbase_input of this BitcoinInput.


        :param coinbase_input: The coinbase_input of this BitcoinInput.  # noqa: E501
        :type: bool
        """

        self._coinbase_input = coinbase_input

    @property
    def details(self):
        """Gets the details of this BitcoinInput.  # noqa: E501

        Details of this transaction input, if requested.  # noqa: E501

        :return: The details of this BitcoinInput.  # noqa: E501
        :rtype: InputDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BitcoinInput.

        Details of this transaction input, if requested.  # noqa: E501

        :param details: The details of this BitcoinInput.  # noqa: E501
        :type: InputDetails
        """

        self._details = details

    @property
    def input_index(self):
        """Gets the input_index of this BitcoinInput.  # noqa: E501

        The position of this input within the transaction (e.g., ordinal in vin).  # noqa: E501

        :return: The input_index of this BitcoinInput.  # noqa: E501
        :rtype: int
        """
        return self._input_index

    @input_index.setter
    def input_index(self, input_index):
        """Sets the input_index of this BitcoinInput.

        The position of this input within the transaction (e.g., ordinal in vin).  # noqa: E501

        :param input_index: The input_index of this BitcoinInput.  # noqa: E501
        :type: int
        """

        self._input_index = input_index

    @property
    def median_time(self):
        """Gets the median_time of this BitcoinInput.  # noqa: E501

        The medianTime of the block that included the transaction output that this input spends.  # noqa: E501

        :return: The median_time of this BitcoinInput.  # noqa: E501
        :rtype: datetime
        """
        return self._median_time

    @median_time.setter
    def median_time(self, median_time):
        """Sets the median_time of this BitcoinInput.

        The medianTime of the block that included the transaction output that this input spends.  # noqa: E501

        :param median_time: The median_time of this BitcoinInput.  # noqa: E501
        :type: datetime
        """

        self._median_time = median_time

    @property
    def miner_time(self):
        """Gets the miner_time of this BitcoinInput.  # noqa: E501

        The minerTime of the block that included the transaction output that this input spends.  # noqa: E501

        :return: The miner_time of this BitcoinInput.  # noqa: E501
        :rtype: datetime
        """
        return self._miner_time

    @miner_time.setter
    def miner_time(self, miner_time):
        """Sets the miner_time of this BitcoinInput.

        The minerTime of the block that included the transaction output that this input spends.  # noqa: E501

        :param miner_time: The miner_time of this BitcoinInput.  # noqa: E501
        :type: datetime
        """

        self._miner_time = miner_time

    @property
    def name(self):
        """Gets the name of this BitcoinInput.  # noqa: E501


        :return: The name of this BitcoinInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BitcoinInput.


        :param name: The name of this BitcoinInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def signatures(self):
        """Gets the signatures of this BitcoinInput.  # noqa: E501

        Number of signatures provided for this input.  # noqa: E501

        :return: The signatures of this BitcoinInput.  # noqa: E501
        :rtype: int
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this BitcoinInput.

        Number of signatures provided for this input.  # noqa: E501

        :param signatures: The signatures of this BitcoinInput.  # noqa: E501
        :type: int
        """

        self._signatures = signatures

    @property
    def transaction_name(self):
        """Gets the transaction_name of this BitcoinInput.  # noqa: E501

        The name of the transaction that supplied this input value.  # noqa: E501

        :return: The transaction_name of this BitcoinInput.  # noqa: E501
        :rtype: str
        """
        return self._transaction_name

    @transaction_name.setter
    def transaction_name(self, transaction_name):
        """Sets the transaction_name of this BitcoinInput.

        The name of the transaction that supplied this input value.  # noqa: E501

        :param transaction_name: The transaction_name of this BitcoinInput.  # noqa: E501
        :type: str
        """

        self._transaction_name = transaction_name

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
        if not isinstance(other, BitcoinInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
