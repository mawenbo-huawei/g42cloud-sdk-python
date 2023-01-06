# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveNodesSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login': 'Login',
        'nodes': 'list[NodeItem]'
    }

    attribute_map = {
        'login': 'login',
        'nodes': 'nodes'
    }

    def __init__(self, login=None, nodes=None):
        """RemoveNodesSpec

        The model defined in g42cloud sdk

        :param login: The param of the RemoveNodesSpec
        :type login: :class:`g42cloudsdkcce.v3.Login`
        :param nodes: The param of the RemoveNodesSpec
        :type nodes: list[:class:`g42cloudsdkcce.v3.NodeItem`]
        """
        
        

        self._login = None
        self._nodes = None
        self.discriminator = None

        self.login = login
        self.nodes = nodes

    @property
    def login(self):
        """Gets the login of this RemoveNodesSpec.

        :return: The login of this RemoveNodesSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this RemoveNodesSpec.

        :param login: The login of this RemoveNodesSpec.
        :type login: :class:`g42cloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def nodes(self):
        """Gets the nodes of this RemoveNodesSpec.

        :return: The nodes of this RemoveNodesSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.NodeItem`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this RemoveNodesSpec.

        :param nodes: The nodes of this RemoveNodesSpec.
        :type nodes: list[:class:`g42cloudsdkcce.v3.NodeItem`]
        """
        self._nodes = nodes

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
        if not isinstance(other, RemoveNodesSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
