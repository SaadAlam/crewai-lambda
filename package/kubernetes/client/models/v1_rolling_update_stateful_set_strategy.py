# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1RollingUpdateStatefulSetStrategy(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'max_unavailable': 'object',
        'partition': 'int'
    }

    attribute_map = {
        'max_unavailable': 'maxUnavailable',
        'partition': 'partition'
    }

    def __init__(self, max_unavailable=None, partition=None, local_vars_configuration=None):  # noqa: E501
        """V1RollingUpdateStatefulSetStrategy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_unavailable = None
        self._partition = None
        self.discriminator = None

        if max_unavailable is not None:
            self.max_unavailable = max_unavailable
        if partition is not None:
            self.partition = partition

    @property
    def max_unavailable(self):
        """Gets the max_unavailable of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501

        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.  # noqa: E501

        :return: The max_unavailable of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501
        :rtype: object
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        """Sets the max_unavailable of this V1RollingUpdateStatefulSetStrategy.

        The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.  # noqa: E501

        :param max_unavailable: The max_unavailable of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501
        :type: object
        """

        self._max_unavailable = max_unavailable

    @property
    def partition(self):
        """Gets the partition of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501

        Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.  # noqa: E501

        :return: The partition of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V1RollingUpdateStatefulSetStrategy.

        Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.  # noqa: E501

        :param partition: The partition of this V1RollingUpdateStatefulSetStrategy.  # noqa: E501
        :type: int
        """

        self._partition = partition

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1RollingUpdateStatefulSetStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RollingUpdateStatefulSetStrategy):
            return True

        return self.to_dict() != other.to_dict()
