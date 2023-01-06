# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'Metadata',
        'spec': 'InstanceRequestSpec'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None):
        """InstanceRequest

        The model defined in g42cloud sdk

        :param kind: The param of the InstanceRequest
        :type kind: str
        :param api_version: The param of the InstanceRequest
        :type api_version: str
        :param metadata: The param of the InstanceRequest
        :type metadata: :class:`g42cloudsdkcce.v3.Metadata`
        :param spec: The param of the InstanceRequest
        :type spec: :class:`g42cloudsdkcce.v3.InstanceRequestSpec`
        """
        
        

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.kind = kind
        self.api_version = api_version
        self.metadata = metadata
        self.spec = spec

    @property
    def kind(self):
        """Gets the kind of this InstanceRequest.

        :return: The kind of this InstanceRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this InstanceRequest.

        :param kind: The kind of this InstanceRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this InstanceRequest.

        :return: The api_version of this InstanceRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this InstanceRequest.

        :param api_version: The api_version of this InstanceRequest.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """Gets the metadata of this InstanceRequest.

        :return: The metadata of this InstanceRequest.
        :rtype: :class:`g42cloudsdkcce.v3.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InstanceRequest.

        :param metadata: The metadata of this InstanceRequest.
        :type metadata: :class:`g42cloudsdkcce.v3.Metadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this InstanceRequest.

        :return: The spec of this InstanceRequest.
        :rtype: :class:`g42cloudsdkcce.v3.InstanceRequestSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this InstanceRequest.

        :param spec: The spec of this InstanceRequest.
        :type spec: :class:`g42cloudsdkcce.v3.InstanceRequestSpec`
        """
        self._spec = spec

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
        if not isinstance(other, InstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
