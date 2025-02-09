# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'id': 'str',
        'statement': 'list[Statement]'
    }

    attribute_map = {
        'version': 'Version',
        'id': 'Id',
        'statement': 'Statement'
    }

    def __init__(self, version=None, id=None, statement=None):
        """TopicAttribute

        The model defined in g42cloud sdk

        :param version: The param of the TopicAttribute
        :type version: str
        :param id: The param of the TopicAttribute
        :type id: str
        :param statement: The param of the TopicAttribute
        :type statement: list[:class:`g42cloudsdksmn.v2.Statement`]
        """
        
        

        self._version = None
        self._id = None
        self._statement = None
        self.discriminator = None

        self.version = version
        self.id = id
        self.statement = statement

    @property
    def version(self):
        """Gets the version of this TopicAttribute.

        :return: The version of this TopicAttribute.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TopicAttribute.

        :param version: The version of this TopicAttribute.
        :type version: str
        """
        self._version = version

    @property
    def id(self):
        """Gets the id of this TopicAttribute.

        :return: The id of this TopicAttribute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopicAttribute.

        :param id: The id of this TopicAttribute.
        :type id: str
        """
        self._id = id

    @property
    def statement(self):
        """Gets the statement of this TopicAttribute.

        :return: The statement of this TopicAttribute.
        :rtype: list[:class:`g42cloudsdksmn.v2.Statement`]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this TopicAttribute.

        :param statement: The statement of this TopicAttribute.
        :type statement: list[:class:`g42cloudsdksmn.v2.Statement`]
        """
        self._statement = statement

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
        if not isinstance(other, TopicAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
