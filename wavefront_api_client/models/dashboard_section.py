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


class DashboardSection(object):
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
        'name': 'str',
        'rows': 'list[DashboardSectionRow]'
    }

    attribute_map = {
        'name': 'name',
        'rows': 'rows'
    }

    def __init__(self, name=None, rows=None):
        """
        DashboardSection - a model defined in Swagger
        """

        self._name = None
        self._rows = None

        self.name = name
        self.rows = rows

    @property
    def name(self):
        """
        Gets the name of this DashboardSection.
        Name of this section

        :return: The name of this DashboardSection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DashboardSection.
        Name of this section

        :param name: The name of this DashboardSection.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rows(self):
        """
        Gets the rows of this DashboardSection.
        Rows of this section

        :return: The rows of this DashboardSection.
        :rtype: list[DashboardSectionRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this DashboardSection.
        Rows of this section

        :param rows: The rows of this DashboardSection.
        :type: list[DashboardSectionRow]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")

        self._rows = rows

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
        if not isinstance(other, DashboardSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
