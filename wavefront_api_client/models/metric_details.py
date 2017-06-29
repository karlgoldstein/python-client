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


class MetricDetails(object):
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
        'host': 'str',
        'last_update': 'int',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'host': 'host',
        'last_update': 'last_update',
        'tags': 'tags'
    }

    def __init__(self, host=None, last_update=None, tags=None):
        """
        MetricDetails - a model defined in Swagger
        """

        self._host = None
        self._last_update = None
        self._tags = None

        if host is not None:
          self.host = host
        if last_update is not None:
          self.last_update = last_update
        if tags is not None:
          self.tags = tags

    @property
    def host(self):
        """
        Gets the host of this MetricDetails.
        The source reporting this metric

        :return: The host of this MetricDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this MetricDetails.
        The source reporting this metric

        :param host: The host of this MetricDetails.
        :type: str
        """

        self._host = host

    @property
    def last_update(self):
        """
        Gets the last_update of this MetricDetails.
        Approximate time of last reporting, in milliseconds since the Unix epoch

        :return: The last_update of this MetricDetails.
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """
        Sets the last_update of this MetricDetails.
        Approximate time of last reporting, in milliseconds since the Unix epoch

        :param last_update: The last_update of this MetricDetails.
        :type: int
        """

        self._last_update = last_update

    @property
    def tags(self):
        """
        Gets the tags of this MetricDetails.
        A key-value map of the point tags associated with this source

        :return: The tags of this MetricDetails.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MetricDetails.
        A key-value map of the point tags associated with this source

        :param tags: The tags of this MetricDetails.
        :type: dict(str, str)
        """

        self._tags = tags

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
        if not isinstance(other, MetricDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
