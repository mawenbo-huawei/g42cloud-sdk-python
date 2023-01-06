# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityGroupRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str',
        'description': 'str',
        'direction': 'str',
        'ethertype': 'str',
        'protocol': 'str',
        'multiport': 'str',
        'remote_ip_prefix': 'str',
        'remote_group_id': 'str',
        'remote_address_group_id': 'str',
        'action': 'str',
        'priority': 'str'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'description': 'description',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'protocol': 'protocol',
        'multiport': 'multiport',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_group_id': 'remote_group_id',
        'remote_address_group_id': 'remote_address_group_id',
        'action': 'action',
        'priority': 'priority'
    }

    def __init__(self, security_group_id=None, description=None, direction=None, ethertype=None, protocol=None, multiport=None, remote_ip_prefix=None, remote_group_id=None, remote_address_group_id=None, action=None, priority=None):
        """CreateSecurityGroupRuleOption

        The model defined in g42cloud sdk

        :param security_group_id: The param of the CreateSecurityGroupRuleOption
        :type security_group_id: str
        :param description: The param of the CreateSecurityGroupRuleOption
        :type description: str
        :param direction: The param of the CreateSecurityGroupRuleOption
        :type direction: str
        :param ethertype: The param of the CreateSecurityGroupRuleOption
        :type ethertype: str
        :param protocol: The param of the CreateSecurityGroupRuleOption
        :type protocol: str
        :param multiport: The param of the CreateSecurityGroupRuleOption
        :type multiport: str
        :param remote_ip_prefix: The param of the CreateSecurityGroupRuleOption
        :type remote_ip_prefix: str
        :param remote_group_id: The param of the CreateSecurityGroupRuleOption
        :type remote_group_id: str
        :param remote_address_group_id: The param of the CreateSecurityGroupRuleOption
        :type remote_address_group_id: str
        :param action: The param of the CreateSecurityGroupRuleOption
        :type action: str
        :param priority: The param of the CreateSecurityGroupRuleOption
        :type priority: str
        """
        
        

        self._security_group_id = None
        self._description = None
        self._direction = None
        self._ethertype = None
        self._protocol = None
        self._multiport = None
        self._remote_ip_prefix = None
        self._remote_group_id = None
        self._remote_address_group_id = None
        self._action = None
        self._priority = None
        self.discriminator = None

        self.security_group_id = security_group_id
        if description is not None:
            self.description = description
        self.direction = direction
        if ethertype is not None:
            self.ethertype = ethertype
        if protocol is not None:
            self.protocol = protocol
        if multiport is not None:
            self.multiport = multiport
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if remote_address_group_id is not None:
            self.remote_address_group_id = remote_address_group_id
        if action is not None:
            self.action = action
        if priority is not None:
            self.priority = priority

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateSecurityGroupRuleOption.

        :return: The security_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateSecurityGroupRuleOption.

        :param security_group_id: The security_group_id of this CreateSecurityGroupRuleOption.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def description(self):
        """Gets the description of this CreateSecurityGroupRuleOption.

        :return: The description of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecurityGroupRuleOption.

        :param description: The description of this CreateSecurityGroupRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        """Gets the direction of this CreateSecurityGroupRuleOption.

        :return: The direction of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CreateSecurityGroupRuleOption.

        :param direction: The direction of this CreateSecurityGroupRuleOption.
        :type direction: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        """Gets the ethertype of this CreateSecurityGroupRuleOption.

        :return: The ethertype of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this CreateSecurityGroupRuleOption.

        :param ethertype: The ethertype of this CreateSecurityGroupRuleOption.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def protocol(self):
        """Gets the protocol of this CreateSecurityGroupRuleOption.

        :return: The protocol of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateSecurityGroupRuleOption.

        :param protocol: The protocol of this CreateSecurityGroupRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def multiport(self):
        """Gets the multiport of this CreateSecurityGroupRuleOption.

        :return: The multiport of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._multiport

    @multiport.setter
    def multiport(self, multiport):
        """Sets the multiport of this CreateSecurityGroupRuleOption.

        :param multiport: The multiport of this CreateSecurityGroupRuleOption.
        :type multiport: str
        """
        self._multiport = multiport

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        :return: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        :param remote_ip_prefix: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this CreateSecurityGroupRuleOption.

        :return: The remote_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this CreateSecurityGroupRuleOption.

        :param remote_group_id: The remote_group_id of this CreateSecurityGroupRuleOption.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_address_group_id(self):
        """Gets the remote_address_group_id of this CreateSecurityGroupRuleOption.

        :return: The remote_address_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_address_group_id

    @remote_address_group_id.setter
    def remote_address_group_id(self, remote_address_group_id):
        """Sets the remote_address_group_id of this CreateSecurityGroupRuleOption.

        :param remote_address_group_id: The remote_address_group_id of this CreateSecurityGroupRuleOption.
        :type remote_address_group_id: str
        """
        self._remote_address_group_id = remote_address_group_id

    @property
    def action(self):
        """Gets the action of this CreateSecurityGroupRuleOption.

        :return: The action of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateSecurityGroupRuleOption.

        :param action: The action of this CreateSecurityGroupRuleOption.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this CreateSecurityGroupRuleOption.

        :return: The priority of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateSecurityGroupRuleOption.

        :param priority: The priority of this CreateSecurityGroupRuleOption.
        :type priority: str
        """
        self._priority = priority

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
        if not isinstance(other, CreateSecurityGroupRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
