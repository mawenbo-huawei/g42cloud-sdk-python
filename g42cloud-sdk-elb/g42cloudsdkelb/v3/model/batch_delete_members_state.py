# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMembersState:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ret_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ret_status': 'ret_status'
    }

    def __init__(self, id=None, ret_status=None):
        """BatchDeleteMembersState

        The model defined in g42cloud sdk

        :param id: The param of the BatchDeleteMembersState
        :type id: str
        :param ret_status: The param of the BatchDeleteMembersState
        :type ret_status: str
        """
        
        

        self._id = None
        self._ret_status = None
        self.discriminator = None

        self.id = id
        self.ret_status = ret_status

    @property
    def id(self):
        """Gets the id of this BatchDeleteMembersState.

        :return: The id of this BatchDeleteMembersState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchDeleteMembersState.

        :param id: The id of this BatchDeleteMembersState.
        :type id: str
        """
        self._id = id

    @property
    def ret_status(self):
        """Gets the ret_status of this BatchDeleteMembersState.

        :return: The ret_status of this BatchDeleteMembersState.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        """Sets the ret_status of this BatchDeleteMembersState.

        :param ret_status: The ret_status of this BatchDeleteMembersState.
        :type ret_status: str
        """
        self._ret_status = ret_status

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
        if not isinstance(other, BatchDeleteMembersState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
