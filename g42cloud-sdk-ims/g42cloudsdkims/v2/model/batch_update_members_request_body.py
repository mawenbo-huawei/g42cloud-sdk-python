# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateMembersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'images': 'list[str]',
        'project_id': 'str',
        'status': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'images': 'images',
        'project_id': 'project_id',
        'status': 'status',
        'vault_id': 'vault_id'
    }

    def __init__(self, images=None, project_id=None, status=None, vault_id=None):
        """BatchUpdateMembersRequestBody

        The model defined in g42cloud sdk

        :param images: The param of the BatchUpdateMembersRequestBody
        :type images: list[str]
        :param project_id: The param of the BatchUpdateMembersRequestBody
        :type project_id: str
        :param status: The param of the BatchUpdateMembersRequestBody
        :type status: str
        :param vault_id: The param of the BatchUpdateMembersRequestBody
        :type vault_id: str
        """
        
        

        self._images = None
        self._project_id = None
        self._status = None
        self._vault_id = None
        self.discriminator = None

        self.images = images
        self.project_id = project_id
        self.status = status
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def images(self):
        """Gets the images of this BatchUpdateMembersRequestBody.

        :return: The images of this BatchUpdateMembersRequestBody.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this BatchUpdateMembersRequestBody.

        :param images: The images of this BatchUpdateMembersRequestBody.
        :type images: list[str]
        """
        self._images = images

    @property
    def project_id(self):
        """Gets the project_id of this BatchUpdateMembersRequestBody.

        :return: The project_id of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchUpdateMembersRequestBody.

        :param project_id: The project_id of this BatchUpdateMembersRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this BatchUpdateMembersRequestBody.

        :return: The status of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpdateMembersRequestBody.

        :param status: The status of this BatchUpdateMembersRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this BatchUpdateMembersRequestBody.

        :return: The vault_id of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this BatchUpdateMembersRequestBody.

        :param vault_id: The vault_id of this BatchUpdateMembersRequestBody.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, BatchUpdateMembersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
