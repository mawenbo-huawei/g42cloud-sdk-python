# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOffSiteInstancesRequest:

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
        'offset': 'object',
        'limit': 'object'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, offset=None, limit=None):
        """ListOffSiteInstancesRequest

        The model defined in g42cloud sdk

        :param x_language: The param of the ListOffSiteInstancesRequest
        :type x_language: str
        :param offset: The param of the ListOffSiteInstancesRequest
        :type offset: object
        :param limit: The param of the ListOffSiteInstancesRequest
        :type limit: object
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListOffSiteInstancesRequest.

        :return: The x_language of this ListOffSiteInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListOffSiteInstancesRequest.

        :param x_language: The x_language of this ListOffSiteInstancesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        """Gets the offset of this ListOffSiteInstancesRequest.

        :return: The offset of this ListOffSiteInstancesRequest.
        :rtype: object
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOffSiteInstancesRequest.

        :param offset: The offset of this ListOffSiteInstancesRequest.
        :type offset: object
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListOffSiteInstancesRequest.

        :return: The limit of this ListOffSiteInstancesRequest.
        :rtype: object
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOffSiteInstancesRequest.

        :param limit: The limit of this ListOffSiteInstancesRequest.
        :type limit: object
        """
        self._limit = limit

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
        if not isinstance(other, ListOffSiteInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
