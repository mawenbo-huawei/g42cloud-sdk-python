# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedirectUrlConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'host': 'str',
        'port': 'str',
        'path': 'str',
        'query': 'str',
        'status_code': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'query': 'query',
        'status_code': 'status_code'
    }

    def __init__(self, protocol=None, host=None, port=None, path=None, query=None, status_code=None):
        """RedirectUrlConfig

        The model defined in g42cloud sdk

        :param protocol: The param of the RedirectUrlConfig
        :type protocol: str
        :param host: The param of the RedirectUrlConfig
        :type host: str
        :param port: The param of the RedirectUrlConfig
        :type port: str
        :param path: The param of the RedirectUrlConfig
        :type path: str
        :param query: The param of the RedirectUrlConfig
        :type query: str
        :param status_code: The param of the RedirectUrlConfig
        :type status_code: str
        """
        
        

        self._protocol = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None
        self._status_code = None
        self.discriminator = None

        self.protocol = protocol
        self.host = host
        self.port = port
        self.path = path
        self.query = query
        self.status_code = status_code

    @property
    def protocol(self):
        """Gets the protocol of this RedirectUrlConfig.

        :return: The protocol of this RedirectUrlConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this RedirectUrlConfig.

        :param protocol: The protocol of this RedirectUrlConfig.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def host(self):
        """Gets the host of this RedirectUrlConfig.

        :return: The host of this RedirectUrlConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this RedirectUrlConfig.

        :param host: The host of this RedirectUrlConfig.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this RedirectUrlConfig.

        :return: The port of this RedirectUrlConfig.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RedirectUrlConfig.

        :param port: The port of this RedirectUrlConfig.
        :type port: str
        """
        self._port = port

    @property
    def path(self):
        """Gets the path of this RedirectUrlConfig.

        :return: The path of this RedirectUrlConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RedirectUrlConfig.

        :param path: The path of this RedirectUrlConfig.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        """Gets the query of this RedirectUrlConfig.

        :return: The query of this RedirectUrlConfig.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this RedirectUrlConfig.

        :param query: The query of this RedirectUrlConfig.
        :type query: str
        """
        self._query = query

    @property
    def status_code(self):
        """Gets the status_code of this RedirectUrlConfig.

        :return: The status_code of this RedirectUrlConfig.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RedirectUrlConfig.

        :param status_code: The status_code of this RedirectUrlConfig.
        :type status_code: str
        """
        self._status_code = status_code

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
        if not isinstance(other, RedirectUrlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
