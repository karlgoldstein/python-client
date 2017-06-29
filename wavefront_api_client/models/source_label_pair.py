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


class SourceLabelPair(object):
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
        'label': 'str',
        'host': 'str',
        'tags': 'dict(str, str)',
        'observed': 'int',
        'firing': 'int'
    }

    attribute_map = {
        'label': 'label',
        'host': 'host',
        'tags': 'tags',
        'observed': 'observed',
        'firing': 'firing'
    }

    def __init__(self, label=None, host=None, tags=None, observed=None, firing=None):
        """
        SourceLabelPair - a model defined in Swagger
        """

        self._label = None
        self._host = None
        self._tags = None
        self._observed = None
        self._firing = None

        if label is not None:
          self.label = label
        if host is not None:
          self.host = host
        if tags is not None:
          self.tags = tags
        if observed is not None:
          self.observed = observed
        if firing is not None:
          self.firing = firing

    @property
    def label(self):
        """
        Gets the label of this SourceLabelPair.

        :return: The label of this SourceLabelPair.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this SourceLabelPair.

        :param label: The label of this SourceLabelPair.
        :type: str
        """

        self._label = label

    @property
    def host(self):
        """
        Gets the host of this SourceLabelPair.
        Source (or host).  \"Source\" and \"host\" are synonyms in current versions of wavefront, but the host terminology is deprecated

        :return: The host of this SourceLabelPair.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this SourceLabelPair.
        Source (or host).  \"Source\" and \"host\" are synonyms in current versions of wavefront, but the host terminology is deprecated

        :param host: The host of this SourceLabelPair.
        :type: str
        """

        self._host = host

    @property
    def tags(self):
        """
        Gets the tags of this SourceLabelPair.

        :return: The tags of this SourceLabelPair.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SourceLabelPair.

        :param tags: The tags of this SourceLabelPair.
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def observed(self):
        """
        Gets the observed of this SourceLabelPair.

        :return: The observed of this SourceLabelPair.
        :rtype: int
        """
        return self._observed

    @observed.setter
    def observed(self, observed):
        """
        Sets the observed of this SourceLabelPair.

        :param observed: The observed of this SourceLabelPair.
        :type: int
        """

        self._observed = observed

    @property
    def firing(self):
        """
        Gets the firing of this SourceLabelPair.

        :return: The firing of this SourceLabelPair.
        :rtype: int
        """
        return self._firing

    @firing.setter
    def firing(self, firing):
        """
        Sets the firing of this SourceLabelPair.

        :param firing: The firing of this SourceLabelPair.
        :type: int
        """

        self._firing = firing

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
        if not isinstance(other, SourceLabelPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
