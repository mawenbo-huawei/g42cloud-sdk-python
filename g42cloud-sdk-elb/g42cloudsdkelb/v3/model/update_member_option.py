# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMemberOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'name': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'weight': 'weight'
    }

    def __init__(self, admin_state_up=None, name=None, weight=None):
        """UpdateMemberOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdateMemberOption
        :type admin_state_up: bool
        :param name: The param of the UpdateMemberOption
        :type name: str
        :param weight: The param of the UpdateMemberOption
        :type weight: int
        """
        
        

        self._admin_state_up = None
        self._name = None
        self._weight = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateMemberOption.

        :return: The admin_state_up of this UpdateMemberOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateMemberOption.

        :param admin_state_up: The admin_state_up of this UpdateMemberOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this UpdateMemberOption.

        :return: The name of this UpdateMemberOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateMemberOption.

        :param name: The name of this UpdateMemberOption.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this UpdateMemberOption.

        :return: The weight of this UpdateMemberOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this UpdateMemberOption.

        :param weight: The weight of this UpdateMemberOption.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, UpdateMemberOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
