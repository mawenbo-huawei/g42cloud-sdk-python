# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenProxyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'node_num': 'int'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_num': 'node_num'
    }

    def __init__(self, flavor_id=None, node_num=None):
        """OpenProxyRequest

        The model defined in g42cloud sdk

        :param flavor_id: The param of the OpenProxyRequest
        :type flavor_id: str
        :param node_num: The param of the OpenProxyRequest
        :type node_num: int
        """
        
        

        self._flavor_id = None
        self._node_num = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if node_num is not None:
            self.node_num = node_num

    @property
    def flavor_id(self):
        """Gets the flavor_id of this OpenProxyRequest.

        :return: The flavor_id of this OpenProxyRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this OpenProxyRequest.

        :param flavor_id: The flavor_id of this OpenProxyRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def node_num(self):
        """Gets the node_num of this OpenProxyRequest.

        :return: The node_num of this OpenProxyRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this OpenProxyRequest.

        :param node_num: The node_num of this OpenProxyRequest.
        :type node_num: int
        """
        self._node_num = node_num

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
        if not isinstance(other, OpenProxyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
