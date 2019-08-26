# coding: utf-8

"""
    Cyber Wars API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GameMapTiles(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'owner': 'int'
    }

    attribute_map = {
        'type': 'type',
        'owner': 'owner'
    }

    def __init__(self, type=None, owner=None):  # noqa: E501
        """GameMapTiles - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._owner = None
        self.discriminator = None

        self.type = type
        self.owner = owner

    @property
    def type(self):
        """Gets the type of this GameMapTiles.  # noqa: E501


        :return: The type of this GameMapTiles.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GameMapTiles.


        :param type: The type of this GameMapTiles.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["concrete", "brick"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def owner(self):
        """Gets the owner of this GameMapTiles.  # noqa: E501


        :return: The owner of this GameMapTiles.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GameMapTiles.


        :param owner: The owner of this GameMapTiles.  # noqa: E501
        :type: int
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501
        if owner is not None and owner < 1:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must be a value greater than or equal to `1`")  # noqa: E501

        self._owner = owner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, GameMapTiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other