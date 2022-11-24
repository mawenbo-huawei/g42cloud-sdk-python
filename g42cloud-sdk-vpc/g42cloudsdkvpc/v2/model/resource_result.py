# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'used': 'int',
        'quota': 'int',
        'min': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'quota': 'quota',
        'min': 'min'
    }

    def __init__(self, type=None, used=None, quota=None, min=None):
        """ResourceResult

        The model defined in g42cloud sdk

        :param type: The param of the ResourceResult
        :type type: str
        :param used: The param of the ResourceResult
        :type used: int
        :param quota: The param of the ResourceResult
        :type quota: int
        :param min: The param of the ResourceResult
        :type min: int
        """
        
        

        self._type = None
        self._used = None
        self._quota = None
        self._min = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.quota = quota
        self.min = min

    @property
    def type(self):
        """Gets the type of this ResourceResult.

        :return: The type of this ResourceResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceResult.

        :param type: The type of this ResourceResult.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this ResourceResult.

        :return: The used of this ResourceResult.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ResourceResult.

        :param used: The used of this ResourceResult.
        :type used: int
        """
        self._used = used

    @property
    def quota(self):
        """Gets the quota of this ResourceResult.

        :return: The quota of this ResourceResult.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ResourceResult.

        :param quota: The quota of this ResourceResult.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this ResourceResult.

        :return: The min of this ResourceResult.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ResourceResult.

        :param min: The min of this ResourceResult.
        :type min: int
        """
        self._min = min

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
        if not isinstance(other, ResourceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
