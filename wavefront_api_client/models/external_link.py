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


class ExternalLink(object):
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
        'id': 'str',
        'description': 'str',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'updater_id': 'str',
        'creator_id': 'str',
        'template': 'str',
        'metric_filter_regex': 'str',
        'source_filter_regex': 'str',
        'point_tag_filter_regexes': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId',
        'creator_id': 'creatorId',
        'template': 'template',
        'metric_filter_regex': 'metricFilterRegex',
        'source_filter_regex': 'sourceFilterRegex',
        'point_tag_filter_regexes': 'pointTagFilterRegexes'
    }

    def __init__(self, name=None, id=None, description=None, created_epoch_millis=None, updated_epoch_millis=None, updater_id=None, creator_id=None, template=None, metric_filter_regex=None, source_filter_regex=None, point_tag_filter_regexes=None):
        """
        ExternalLink - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._description = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self._creator_id = None
        self._template = None
        self._metric_filter_regex = None
        self._source_filter_regex = None
        self._point_tag_filter_regexes = None

        self.name = name
        if id is not None:
          self.id = id
        self.description = description
        if created_epoch_millis is not None:
          self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
          self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
          self.updater_id = updater_id
        if creator_id is not None:
          self.creator_id = creator_id
        self.template = template
        if metric_filter_regex is not None:
          self.metric_filter_regex = metric_filter_regex
        if source_filter_regex is not None:
          self.source_filter_regex = source_filter_regex
        if point_tag_filter_regexes is not None:
          self.point_tag_filter_regexes = point_tag_filter_regexes

    @property
    def name(self):
        """
        Gets the name of this ExternalLink.
        Name of the external link.  Will be displayed in context (right-click) menus on charts

        :return: The name of this ExternalLink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalLink.
        Name of the external link.  Will be displayed in context (right-click) menus on charts

        :param name: The name of this ExternalLink.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this ExternalLink.

        :return: The id of this ExternalLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalLink.

        :param id: The id of this ExternalLink.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this ExternalLink.
        Human-readable description for this external link

        :return: The description of this ExternalLink.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExternalLink.
        Human-readable description for this external link

        :param description: The description of this ExternalLink.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def created_epoch_millis(self):
        """
        Gets the created_epoch_millis of this ExternalLink.

        :return: The created_epoch_millis of this ExternalLink.
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """
        Sets the created_epoch_millis of this ExternalLink.

        :param created_epoch_millis: The created_epoch_millis of this ExternalLink.
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """
        Gets the updated_epoch_millis of this ExternalLink.

        :return: The updated_epoch_millis of this ExternalLink.
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """
        Sets the updated_epoch_millis of this ExternalLink.

        :param updated_epoch_millis: The updated_epoch_millis of this ExternalLink.
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """
        Gets the updater_id of this ExternalLink.

        :return: The updater_id of this ExternalLink.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """
        Sets the updater_id of this ExternalLink.

        :param updater_id: The updater_id of this ExternalLink.
        :type: str
        """

        self._updater_id = updater_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this ExternalLink.

        :return: The creator_id of this ExternalLink.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this ExternalLink.

        :param creator_id: The creator_id of this ExternalLink.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def template(self):
        """
        Gets the template of this ExternalLink.
        The mustache template for this link.  This template must expand to a full URL, including scheme, origin, etc

        :return: The template of this ExternalLink.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ExternalLink.
        The mustache template for this link.  This template must expand to a full URL, including scheme, origin, etc

        :param template: The template of this ExternalLink.
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

    @property
    def metric_filter_regex(self):
        """
        Gets the metric_filter_regex of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed

        :return: The metric_filter_regex of this ExternalLink.
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """
        Sets the metric_filter_regex of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed

        :param metric_filter_regex: The metric_filter_regex of this ExternalLink.
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def source_filter_regex(self):
        """
        Gets the source_filter_regex of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed

        :return: The source_filter_regex of this ExternalLink.
        :rtype: str
        """
        return self._source_filter_regex

    @source_filter_regex.setter
    def source_filter_regex(self, source_filter_regex):
        """
        Sets the source_filter_regex of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed

        :param source_filter_regex: The source_filter_regex of this ExternalLink.
        :type: str
        """

        self._source_filter_regex = source_filter_regex

    @property
    def point_tag_filter_regexes(self):
        """
        Gets the point_tag_filter_regexes of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed

        :return: The point_tag_filter_regexes of this ExternalLink.
        :rtype: dict(str, str)
        """
        return self._point_tag_filter_regexes

    @point_tag_filter_regexes.setter
    def point_tag_filter_regexes(self, point_tag_filter_regexes):
        """
        Sets the point_tag_filter_regexes of this ExternalLink.
        Controls whether a link displayed in the context menu of a highlighted series.  This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed

        :param point_tag_filter_regexes: The point_tag_filter_regexes of this ExternalLink.
        :type: dict(str, str)
        """

        self._point_tag_filter_regexes = point_tag_filter_regexes

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
        if not isinstance(other, ExternalLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
