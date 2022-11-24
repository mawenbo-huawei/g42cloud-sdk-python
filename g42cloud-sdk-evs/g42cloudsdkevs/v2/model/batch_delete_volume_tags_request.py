# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteVolumeTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'body': 'BatchDeleteVolumeTagsRequestBody'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'body': 'body'
    }

    def __init__(self, volume_id=None, body=None):
        """BatchDeleteVolumeTagsRequest

        The model defined in g42cloud sdk

        :param volume_id: The param of the BatchDeleteVolumeTagsRequest
        :type volume_id: str
        :param body: The param of the BatchDeleteVolumeTagsRequest
        :type body: :class:`g42cloudsdkevs.v2.BatchDeleteVolumeTagsRequestBody`
        """
        
        

        self._volume_id = None
        self._body = None
        self.discriminator = None

        self.volume_id = volume_id
        if body is not None:
            self.body = body

    @property
    def volume_id(self):
        """Gets the volume_id of this BatchDeleteVolumeTagsRequest.

        :return: The volume_id of this BatchDeleteVolumeTagsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this BatchDeleteVolumeTagsRequest.

        :param volume_id: The volume_id of this BatchDeleteVolumeTagsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def body(self):
        """Gets the body of this BatchDeleteVolumeTagsRequest.

        :return: The body of this BatchDeleteVolumeTagsRequest.
        :rtype: :class:`g42cloudsdkevs.v2.BatchDeleteVolumeTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteVolumeTagsRequest.

        :param body: The body of this BatchDeleteVolumeTagsRequest.
        :type body: :class:`g42cloudsdkevs.v2.BatchDeleteVolumeTagsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchDeleteVolumeTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
