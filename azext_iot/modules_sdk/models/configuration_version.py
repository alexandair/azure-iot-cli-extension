# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationVersion(Model):
    """ConfigurationVersion.

    :param configuration_id:
    :type configuration_id: str
    :param internal_version:
    :type internal_version: str
    :param device_version:
    :type device_version: long
    :param configuration_type: Possible values include: 'Exclusive'
    :type configuration_type: str or :class:`ConfigurationType
     <iothubclient.models.ConfigurationType>`
    :param status: Possible values include: 'None', 'Targeted', 'Applied'
    :type status: str or :class:`ConfigurationStatus
     <iothubclient.models.ConfigurationStatus>`
    """

    _attribute_map = {
        'configuration_id': {'key': 'ConfigurationId', 'type': 'str'},
        'internal_version': {'key': 'InternalVersion', 'type': 'str'},
        'device_version': {'key': 'DeviceVersion', 'type': 'long'},
        'configuration_type': {'key': 'ConfigurationType', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
    }

    def __init__(self, configuration_id=None, internal_version=None, device_version=None, configuration_type=None, status=None):
        self.configuration_id = configuration_id
        self.internal_version = internal_version
        self.device_version = device_version
        self.configuration_type = configuration_type
        self.status = status
