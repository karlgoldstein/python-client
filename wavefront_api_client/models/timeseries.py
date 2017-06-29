# coding: utf-8

"""
    Wavefront Public API

    <p>Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront UI you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Timeseries(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'tags': 'dict(str, str)',
        'points': 'list[Point]'
    }

    attribute_map = {
        'tags': 'tags',
        'points': 'points'
    }

    def __init__(self, tags=None, points=None):
        """
        Timeseries - a model defined in Swagger
        """

        self._tags = None
        self._points = None

        if tags is not None:
          self.tags = tags
        self.points = points

    @property
    def tags(self):
        """
        Gets the tags of this Timeseries.
        Associated tags of the time series

        :return: The tags of this Timeseries.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Timeseries.
        Associated tags of the time series

        :param tags: The tags of this Timeseries.
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def points(self):
        """
        Gets the points of this Timeseries.

        :return: The points of this Timeseries.
        :rtype: list[Point]
        """
        return self._points

    @points.setter
    def points(self, points):
        """
        Sets the points of this Timeseries.

        :param points: The points of this Timeseries.
        :type: list[Point]
        """
        if points is None:
            raise ValueError("Invalid value for `points`, must not be `None`")

        self._points = points

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Timeseries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
