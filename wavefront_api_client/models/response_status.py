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


class ResponseStatus(object):
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
        'result': 'str',
        'message': 'str',
        'code': 'int'
    }

    attribute_map = {
        'result': 'result',
        'message': 'message',
        'code': 'code'
    }

    def __init__(self, result=None, message=None, code=None):
        """
        ResponseStatus - a model defined in Swagger
        """

        self._result = None
        self._message = None
        self._code = None

        self.result = result
        if message is not None:
          self.message = message
        self.code = code

    @property
    def result(self):
        """
        Gets the result of this ResponseStatus.

        :return: The result of this ResponseStatus.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this ResponseStatus.

        :param result: The result of this ResponseStatus.
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")
        allowed_values = ["OK", "ERROR"]
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def message(self):
        """
        Gets the message of this ResponseStatus.
        Descriptive message of the status of this response

        :return: The message of this ResponseStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResponseStatus.
        Descriptive message of the status of this response

        :param message: The message of this ResponseStatus.
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """
        Gets the code of this ResponseStatus.
        HTTP Response code corresponding to this response

        :return: The code of this ResponseStatus.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ResponseStatus.
        HTTP Response code corresponding to this response

        :param code: The code of this ResponseStatus.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

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
        if not isinstance(other, ResponseStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
