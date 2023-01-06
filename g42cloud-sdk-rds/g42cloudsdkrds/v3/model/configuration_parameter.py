# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'restart_required': 'bool',
        'readonly': 'bool',
        'value_range': 'str',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'restart_required': 'restart_required',
        'readonly': 'readonly',
        'value_range': 'value_range',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, restart_required=None, readonly=None, value_range=None, type=None, description=None):
        """ConfigurationParameter

        The model defined in g42cloud sdk

        :param name: The param of the ConfigurationParameter
        :type name: str
        :param value: The param of the ConfigurationParameter
        :type value: str
        :param restart_required: The param of the ConfigurationParameter
        :type restart_required: bool
        :param readonly: The param of the ConfigurationParameter
        :type readonly: bool
        :param value_range: The param of the ConfigurationParameter
        :type value_range: str
        :param type: The param of the ConfigurationParameter
        :type type: str
        :param description: The param of the ConfigurationParameter
        :type description: str
        """
        
        

        self._name = None
        self._value = None
        self._restart_required = None
        self._readonly = None
        self._value_range = None
        self._type = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.restart_required = restart_required
        self.readonly = readonly
        self.value_range = value_range
        self.type = type
        self.description = description

    @property
    def name(self):
        """Gets the name of this ConfigurationParameter.

        :return: The name of this ConfigurationParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationParameter.

        :param name: The name of this ConfigurationParameter.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ConfigurationParameter.

        :return: The value of this ConfigurationParameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConfigurationParameter.

        :param value: The value of this ConfigurationParameter.
        :type value: str
        """
        self._value = value

    @property
    def restart_required(self):
        """Gets the restart_required of this ConfigurationParameter.

        :return: The restart_required of this ConfigurationParameter.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        """Sets the restart_required of this ConfigurationParameter.

        :param restart_required: The restart_required of this ConfigurationParameter.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def readonly(self):
        """Gets the readonly of this ConfigurationParameter.

        :return: The readonly of this ConfigurationParameter.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this ConfigurationParameter.

        :param readonly: The readonly of this ConfigurationParameter.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def value_range(self):
        """Gets the value_range of this ConfigurationParameter.

        :return: The value_range of this ConfigurationParameter.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ConfigurationParameter.

        :param value_range: The value_range of this ConfigurationParameter.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def type(self):
        """Gets the type of this ConfigurationParameter.

        :return: The type of this ConfigurationParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigurationParameter.

        :param type: The type of this ConfigurationParameter.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ConfigurationParameter.

        :return: The description of this ConfigurationParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationParameter.

        :param description: The description of this ConfigurationParameter.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConfigurationParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
