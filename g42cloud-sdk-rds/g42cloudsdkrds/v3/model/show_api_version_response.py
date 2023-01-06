# coding: utf-8

import re
import six


from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'ApiVersion',
        'version': 'ApiVersion'
    }

    attribute_map = {
        'versions': 'versions',
        'version': 'version'
    }

    def __init__(self, versions=None, version=None):
        """ShowApiVersionResponse

        The model defined in g42cloud sdk

        :param versions: The param of the ShowApiVersionResponse
        :type versions: :class:`g42cloudsdkrds.v3.ApiVersion`
        :param version: The param of the ShowApiVersionResponse
        :type version: :class:`g42cloudsdkrds.v3.ApiVersion`
        """
        
        super(ShowApiVersionResponse, self).__init__()

        self._versions = None
        self._version = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if version is not None:
            self.version = version

    @property
    def versions(self):
        """Gets the versions of this ShowApiVersionResponse.

        :return: The versions of this ShowApiVersionResponse.
        :rtype: :class:`g42cloudsdkrds.v3.ApiVersion`
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ShowApiVersionResponse.

        :param versions: The versions of this ShowApiVersionResponse.
        :type versions: :class:`g42cloudsdkrds.v3.ApiVersion`
        """
        self._versions = versions

    @property
    def version(self):
        """Gets the version of this ShowApiVersionResponse.

        :return: The version of this ShowApiVersionResponse.
        :rtype: :class:`g42cloudsdkrds.v3.ApiVersion`
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowApiVersionResponse.

        :param version: The version of this ShowApiVersionResponse.
        :type version: :class:`g42cloudsdkrds.v3.ApiVersion`
        """
        self._version = version

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
        if not isinstance(other, ShowApiVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
