# coding: utf-8

import re
import six


from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogtanksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logtanks': 'list[Logtank]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'logtanks': 'logtanks',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, logtanks=None, page_info=None, request_id=None):
        """ListLogtanksResponse

        The model defined in g42cloud sdk

        :param logtanks: The param of the ListLogtanksResponse
        :type logtanks: list[:class:`g42cloudsdkelb.v3.Logtank`]
        :param page_info: The param of the ListLogtanksResponse
        :type page_info: :class:`g42cloudsdkelb.v3.PageInfo`
        :param request_id: The param of the ListLogtanksResponse
        :type request_id: str
        """
        
        super(ListLogtanksResponse, self).__init__()

        self._logtanks = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if logtanks is not None:
            self.logtanks = logtanks
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def logtanks(self):
        """Gets the logtanks of this ListLogtanksResponse.

        :return: The logtanks of this ListLogtanksResponse.
        :rtype: list[:class:`g42cloudsdkelb.v3.Logtank`]
        """
        return self._logtanks

    @logtanks.setter
    def logtanks(self, logtanks):
        """Sets the logtanks of this ListLogtanksResponse.

        :param logtanks: The logtanks of this ListLogtanksResponse.
        :type logtanks: list[:class:`g42cloudsdkelb.v3.Logtank`]
        """
        self._logtanks = logtanks

    @property
    def page_info(self):
        """Gets the page_info of this ListLogtanksResponse.

        :return: The page_info of this ListLogtanksResponse.
        :rtype: :class:`g42cloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListLogtanksResponse.

        :param page_info: The page_info of this ListLogtanksResponse.
        :type page_info: :class:`g42cloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListLogtanksResponse.

        :return: The request_id of this ListLogtanksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListLogtanksResponse.

        :param request_id: The request_id of this ListLogtanksResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListLogtanksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
