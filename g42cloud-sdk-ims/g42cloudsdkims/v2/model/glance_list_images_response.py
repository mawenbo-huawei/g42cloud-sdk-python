# coding: utf-8

import re
import six


from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceListImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'first': 'str',
        'images': 'list[GlanceShowImageResponseBody]',
        'schema': 'str',
        'next': 'str'
    }

    attribute_map = {
        'first': 'first',
        'images': 'images',
        'schema': 'schema',
        'next': 'next'
    }

    def __init__(self, first=None, images=None, schema=None, next=None):
        """GlanceListImagesResponse

        The model defined in g42cloud sdk

        :param first: The param of the GlanceListImagesResponse
        :type first: str
        :param images: The param of the GlanceListImagesResponse
        :type images: list[:class:`g42cloudsdkims.v2.GlanceShowImageResponseBody`]
        :param schema: The param of the GlanceListImagesResponse
        :type schema: str
        :param next: The param of the GlanceListImagesResponse
        :type next: str
        """
        
        super(GlanceListImagesResponse, self).__init__()

        self._first = None
        self._images = None
        self._schema = None
        self._next = None
        self.discriminator = None

        if first is not None:
            self.first = first
        if images is not None:
            self.images = images
        if schema is not None:
            self.schema = schema
        if next is not None:
            self.next = next

    @property
    def first(self):
        """Gets the first of this GlanceListImagesResponse.

        :return: The first of this GlanceListImagesResponse.
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this GlanceListImagesResponse.

        :param first: The first of this GlanceListImagesResponse.
        :type first: str
        """
        self._first = first

    @property
    def images(self):
        """Gets the images of this GlanceListImagesResponse.

        :return: The images of this GlanceListImagesResponse.
        :rtype: list[:class:`g42cloudsdkims.v2.GlanceShowImageResponseBody`]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this GlanceListImagesResponse.

        :param images: The images of this GlanceListImagesResponse.
        :type images: list[:class:`g42cloudsdkims.v2.GlanceShowImageResponseBody`]
        """
        self._images = images

    @property
    def schema(self):
        """Gets the schema of this GlanceListImagesResponse.

        :return: The schema of this GlanceListImagesResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this GlanceListImagesResponse.

        :param schema: The schema of this GlanceListImagesResponse.
        :type schema: str
        """
        self._schema = schema

    @property
    def next(self):
        """Gets the next of this GlanceListImagesResponse.

        :return: The next of this GlanceListImagesResponse.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this GlanceListImagesResponse.

        :param next: The next of this GlanceListImagesResponse.
        :type next: str
        """
        self._next = next

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
        if not isinstance(other, GlanceListImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
