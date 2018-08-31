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


class OutputDetails(object):
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
        'script': 'str',
        'script_type': 'str'
    }

    attribute_map = {
        'script': 'script',
        'script_type': 'scriptType'
    }

    def __init__(self, script=None, script_type=None):  # noqa: E501
        """OutputDetails - a model defined in Swagger"""  # noqa: E501

        self._script = None
        self._script_type = None
        self.discriminator = None

        if script is not None:
            self.script = script
        if script_type is not None:
            self.script_type = script_type

    @property
    def script(self):
        """Gets the script of this OutputDetails.  # noqa: E501

        ASM Locking Script of of this transaction.  # noqa: E501

        :return: The script of this OutputDetails.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this OutputDetails.

        ASM Locking Script of of this transaction.  # noqa: E501

        :param script: The script of this OutputDetails.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def script_type(self):
        """Gets the script_type of this OutputDetails.  # noqa: E501

        The type of locking script employed.  # noqa: E501

        :return: The script_type of this OutputDetails.  # noqa: E501
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this OutputDetails.

        The type of locking script employed.  # noqa: E501

        :param script_type: The script_type of this OutputDetails.  # noqa: E501
        :type: str
        """

        self._script_type = script_type

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
        if not isinstance(other, OutputDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
