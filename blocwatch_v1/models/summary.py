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


class Summary(object):
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
        'inputs_count': 'int',
        'outputs_count': 'int',
        'transaction_value': 'float'
    }

    attribute_map = {
        'inputs_count': 'inputsCount',
        'outputs_count': 'outputsCount',
        'transaction_value': 'transactionValue'
    }

    def __init__(self, inputs_count=None, outputs_count=None, transaction_value=None):  # noqa: E501
        """Summary - a model defined in Swagger"""  # noqa: E501

        self._inputs_count = None
        self._outputs_count = None
        self._transaction_value = None
        self.discriminator = None

        if inputs_count is not None:
            self.inputs_count = inputs_count
        if outputs_count is not None:
            self.outputs_count = outputs_count
        if transaction_value is not None:
            self.transaction_value = transaction_value

    @property
    def inputs_count(self):
        """Gets the inputs_count of this Summary.  # noqa: E501


        :return: The inputs_count of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._inputs_count

    @inputs_count.setter
    def inputs_count(self, inputs_count):
        """Sets the inputs_count of this Summary.


        :param inputs_count: The inputs_count of this Summary.  # noqa: E501
        :type: int
        """

        self._inputs_count = inputs_count

    @property
    def outputs_count(self):
        """Gets the outputs_count of this Summary.  # noqa: E501


        :return: The outputs_count of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._outputs_count

    @outputs_count.setter
    def outputs_count(self, outputs_count):
        """Sets the outputs_count of this Summary.


        :param outputs_count: The outputs_count of this Summary.  # noqa: E501
        :type: int
        """

        self._outputs_count = outputs_count

    @property
    def transaction_value(self):
        """Gets the transaction_value of this Summary.  # noqa: E501


        :return: The transaction_value of this Summary.  # noqa: E501
        :rtype: float
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this Summary.


        :param transaction_value: The transaction_value of this Summary.  # noqa: E501
        :type: float
        """

        self._transaction_value = transaction_value

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
        if not isinstance(other, Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
