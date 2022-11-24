# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyConfigurationAsyncRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'config_id': 'str',
        'body': 'ApplyConfigurationRequest'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'config_id': 'config_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, config_id=None, body=None):
        """ApplyConfigurationAsyncRequest

        The model defined in g42cloud sdk

        :param x_language: The param of the ApplyConfigurationAsyncRequest
        :type x_language: str
        :param config_id: The param of the ApplyConfigurationAsyncRequest
        :type config_id: str
        :param body: The param of the ApplyConfigurationAsyncRequest
        :type body: :class:`g42cloudsdkrds.v3.ApplyConfigurationRequest`
        """
        
        

        self._x_language = None
        self._config_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.config_id = config_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this ApplyConfigurationAsyncRequest.

        :return: The x_language of this ApplyConfigurationAsyncRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ApplyConfigurationAsyncRequest.

        :param x_language: The x_language of this ApplyConfigurationAsyncRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def config_id(self):
        """Gets the config_id of this ApplyConfigurationAsyncRequest.

        :return: The config_id of this ApplyConfigurationAsyncRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this ApplyConfigurationAsyncRequest.

        :param config_id: The config_id of this ApplyConfigurationAsyncRequest.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def body(self):
        """Gets the body of this ApplyConfigurationAsyncRequest.

        :return: The body of this ApplyConfigurationAsyncRequest.
        :rtype: :class:`g42cloudsdkrds.v3.ApplyConfigurationRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ApplyConfigurationAsyncRequest.

        :param body: The body of this ApplyConfigurationAsyncRequest.
        :type body: :class:`g42cloudsdkrds.v3.ApplyConfigurationRequest`
        """
        self._body = body

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApplyConfigurationAsyncRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
