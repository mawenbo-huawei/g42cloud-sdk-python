# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_type': 'str',
        'event_users': 'list[str]',
        'event_sources': 'list[str]',
        'event_info': 'list[EventInfoDetail]',
        'meta_data': 'TotalMetaData'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_type': 'event_type',
        'event_users': 'event_users',
        'event_sources': 'event_sources',
        'event_info': 'event_info',
        'meta_data': 'meta_data'
    }

    def __init__(self, event_name=None, event_type=None, event_users=None, event_sources=None, event_info=None, meta_data=None):
        """ListEventDetailResponse

        The model defined in g42cloud sdk

        :param event_name: The param of the ListEventDetailResponse
        :type event_name: str
        :param event_type: The param of the ListEventDetailResponse
        :type event_type: str
        :param event_users: The param of the ListEventDetailResponse
        :type event_users: list[str]
        :param event_sources: The param of the ListEventDetailResponse
        :type event_sources: list[str]
        :param event_info: The param of the ListEventDetailResponse
        :type event_info: list[:class:`g42cloudsdkces.v1.EventInfoDetail`]
        :param meta_data: The param of the ListEventDetailResponse
        :type meta_data: :class:`g42cloudsdkces.v1.TotalMetaData`
        """
        
        super(ListEventDetailResponse, self).__init__()

        self._event_name = None
        self._event_type = None
        self._event_users = None
        self._event_sources = None
        self._event_info = None
        self._meta_data = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if event_users is not None:
            self.event_users = event_users
        if event_sources is not None:
            self.event_sources = event_sources
        if event_info is not None:
            self.event_info = event_info
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def event_name(self):
        """Gets the event_name of this ListEventDetailResponse.

        :return: The event_name of this ListEventDetailResponse.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this ListEventDetailResponse.

        :param event_name: The event_name of this ListEventDetailResponse.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        """Gets the event_type of this ListEventDetailResponse.

        :return: The event_type of this ListEventDetailResponse.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListEventDetailResponse.

        :param event_type: The event_type of this ListEventDetailResponse.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_users(self):
        """Gets the event_users of this ListEventDetailResponse.

        :return: The event_users of this ListEventDetailResponse.
        :rtype: list[str]
        """
        return self._event_users

    @event_users.setter
    def event_users(self, event_users):
        """Sets the event_users of this ListEventDetailResponse.

        :param event_users: The event_users of this ListEventDetailResponse.
        :type event_users: list[str]
        """
        self._event_users = event_users

    @property
    def event_sources(self):
        """Gets the event_sources of this ListEventDetailResponse.

        :return: The event_sources of this ListEventDetailResponse.
        :rtype: list[str]
        """
        return self._event_sources

    @event_sources.setter
    def event_sources(self, event_sources):
        """Sets the event_sources of this ListEventDetailResponse.

        :param event_sources: The event_sources of this ListEventDetailResponse.
        :type event_sources: list[str]
        """
        self._event_sources = event_sources

    @property
    def event_info(self):
        """Gets the event_info of this ListEventDetailResponse.

        :return: The event_info of this ListEventDetailResponse.
        :rtype: list[:class:`g42cloudsdkces.v1.EventInfoDetail`]
        """
        return self._event_info

    @event_info.setter
    def event_info(self, event_info):
        """Sets the event_info of this ListEventDetailResponse.

        :param event_info: The event_info of this ListEventDetailResponse.
        :type event_info: list[:class:`g42cloudsdkces.v1.EventInfoDetail`]
        """
        self._event_info = event_info

    @property
    def meta_data(self):
        """Gets the meta_data of this ListEventDetailResponse.

        :return: The meta_data of this ListEventDetailResponse.
        :rtype: :class:`g42cloudsdkces.v1.TotalMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListEventDetailResponse.

        :param meta_data: The meta_data of this ListEventDetailResponse.
        :type meta_data: :class:`g42cloudsdkces.v1.TotalMetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListEventDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
