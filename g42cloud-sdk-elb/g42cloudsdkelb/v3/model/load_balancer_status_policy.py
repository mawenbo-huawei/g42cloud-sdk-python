# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatusPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'id': 'str',
        'provisioning_status': 'str',
        'name': 'str',
        'rules': 'list[LoadBalancerStatusL7Rule]'
    }

    attribute_map = {
        'action': 'action',
        'id': 'id',
        'provisioning_status': 'provisioning_status',
        'name': 'name',
        'rules': 'rules'
    }

    def __init__(self, action=None, id=None, provisioning_status=None, name=None, rules=None):
        """LoadBalancerStatusPolicy

        The model defined in g42cloud sdk

        :param action: The param of the LoadBalancerStatusPolicy
        :type action: str
        :param id: The param of the LoadBalancerStatusPolicy
        :type id: str
        :param provisioning_status: The param of the LoadBalancerStatusPolicy
        :type provisioning_status: str
        :param name: The param of the LoadBalancerStatusPolicy
        :type name: str
        :param rules: The param of the LoadBalancerStatusPolicy
        :type rules: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusL7Rule`]
        """
        
        

        self._action = None
        self._id = None
        self._provisioning_status = None
        self._name = None
        self._rules = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if id is not None:
            self.id = id
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules

    @property
    def action(self):
        """Gets the action of this LoadBalancerStatusPolicy.

        :return: The action of this LoadBalancerStatusPolicy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this LoadBalancerStatusPolicy.

        :param action: The action of this LoadBalancerStatusPolicy.
        :type action: str
        """
        self._action = action

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusPolicy.

        :return: The id of this LoadBalancerStatusPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusPolicy.

        :param id: The id of this LoadBalancerStatusPolicy.
        :type id: str
        """
        self._id = id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusPolicy.

        :return: The provisioning_status of this LoadBalancerStatusPolicy.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusPolicy.

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusPolicy.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusPolicy.

        :return: The name of this LoadBalancerStatusPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusPolicy.

        :param name: The name of this LoadBalancerStatusPolicy.
        :type name: str
        """
        self._name = name

    @property
    def rules(self):
        """Gets the rules of this LoadBalancerStatusPolicy.

        :return: The rules of this LoadBalancerStatusPolicy.
        :rtype: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusL7Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this LoadBalancerStatusPolicy.

        :param rules: The rules of this LoadBalancerStatusPolicy.
        :type rules: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusL7Rule`]
        """
        self._rules = rules

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
        if not isinstance(other, LoadBalancerStatusPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
