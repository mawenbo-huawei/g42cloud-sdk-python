# coding: utf-8

import re
import six


from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListListenersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'page_info': 'PageInfo',
        'listeners': 'list[Listener]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'listeners': 'listeners'
    }

    def __init__(self, request_id=None, page_info=None, listeners=None):
        """ListListenersResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the ListListenersResponse
        :type request_id: str
        :param page_info: The param of the ListListenersResponse
        :type page_info: :class:`g42cloudsdkelb.v3.PageInfo`
        :param listeners: The param of the ListListenersResponse
        :type listeners: list[:class:`g42cloudsdkelb.v3.Listener`]
        """
        
        super(ListListenersResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._listeners = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        if listeners is not None:
            self.listeners = listeners

    @property
    def request_id(self):
        """Gets the request_id of this ListListenersResponse.

        :return: The request_id of this ListListenersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListListenersResponse.

        :param request_id: The request_id of this ListListenersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListListenersResponse.

        :return: The page_info of this ListListenersResponse.
        :rtype: :class:`g42cloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListListenersResponse.

        :param page_info: The page_info of this ListListenersResponse.
        :type page_info: :class:`g42cloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def listeners(self):
        """Gets the listeners of this ListListenersResponse.

        :return: The listeners of this ListListenersResponse.
        :rtype: list[:class:`g42cloudsdkelb.v3.Listener`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this ListListenersResponse.

        :param listeners: The listeners of this ListListenersResponse.
        :type listeners: list[:class:`g42cloudsdkelb.v3.Listener`]
        """
        self._listeners = listeners

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
        if not isinstance(other, ListListenersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
