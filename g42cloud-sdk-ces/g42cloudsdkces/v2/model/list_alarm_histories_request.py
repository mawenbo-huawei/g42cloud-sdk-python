# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'status': 'str',
        'level': 'int',
        'namespace': 'str',
        'resource_id': 'str',
        '_from': 'str',
        'to': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'status': 'status',
        'level': 'level',
        'namespace': 'namespace',
        'resource_id': 'resource_id',
        '_from': 'from',
        'to': 'to',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, alarm_id=None, name=None, status=None, level=None, namespace=None, resource_id=None, _from=None, to=None, offset=None, limit=None):
        """ListAlarmHistoriesRequest

        The model defined in g42cloud sdk

        :param alarm_id: The param of the ListAlarmHistoriesRequest
        :type alarm_id: str
        :param name: The param of the ListAlarmHistoriesRequest
        :type name: str
        :param status: The param of the ListAlarmHistoriesRequest
        :type status: str
        :param level: The param of the ListAlarmHistoriesRequest
        :type level: int
        :param namespace: The param of the ListAlarmHistoriesRequest
        :type namespace: str
        :param resource_id: The param of the ListAlarmHistoriesRequest
        :type resource_id: str
        :param _from: The param of the ListAlarmHistoriesRequest
        :type _from: str
        :param to: The param of the ListAlarmHistoriesRequest
        :type to: str
        :param offset: The param of the ListAlarmHistoriesRequest
        :type offset: int
        :param limit: The param of the ListAlarmHistoriesRequest
        :type limit: int
        """
        
        

        self._alarm_id = None
        self._name = None
        self._status = None
        self._level = None
        self._namespace = None
        self._resource_id = None
        self.__from = None
        self._to = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if level is not None:
            self.level = level
        if namespace is not None:
            self.namespace = namespace
        if resource_id is not None:
            self.resource_id = resource_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmHistoriesRequest.

        :return: The alarm_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmHistoriesRequest.

        :param alarm_id: The alarm_id of this ListAlarmHistoriesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this ListAlarmHistoriesRequest.

        :return: The name of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAlarmHistoriesRequest.

        :param name: The name of this ListAlarmHistoriesRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListAlarmHistoriesRequest.

        :return: The status of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAlarmHistoriesRequest.

        :param status: The status of this ListAlarmHistoriesRequest.
        :type status: str
        """
        self._status = status

    @property
    def level(self):
        """Gets the level of this ListAlarmHistoriesRequest.

        :return: The level of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListAlarmHistoriesRequest.

        :param level: The level of this ListAlarmHistoriesRequest.
        :type level: int
        """
        self._level = level

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmHistoriesRequest.

        :return: The namespace of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmHistoriesRequest.

        :param namespace: The namespace of this ListAlarmHistoriesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_id(self):
        """Gets the resource_id of this ListAlarmHistoriesRequest.

        :return: The resource_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListAlarmHistoriesRequest.

        :param resource_id: The resource_id of this ListAlarmHistoriesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def _from(self):
        """Gets the _from of this ListAlarmHistoriesRequest.

        :return: The _from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListAlarmHistoriesRequest.

        :param _from: The _from of this ListAlarmHistoriesRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListAlarmHistoriesRequest.

        :return: The to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListAlarmHistoriesRequest.

        :param to: The to of this ListAlarmHistoriesRequest.
        :type to: str
        """
        self._to = to

    @property
    def offset(self):
        """Gets the offset of this ListAlarmHistoriesRequest.

        :return: The offset of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmHistoriesRequest.

        :param offset: The offset of this ListAlarmHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlarmHistoriesRequest.

        :return: The limit of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmHistoriesRequest.

        :param limit: The limit of this ListAlarmHistoriesRequest.
        :type limit: int
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
        if not isinstance(other, ListAlarmHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
