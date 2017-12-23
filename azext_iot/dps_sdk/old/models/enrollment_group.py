# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnrollmentGroup(Model):
    """The device enrollment record.

    :param enrollment_group_id:
    :type enrollment_group_id: str
    :param attestation:
    :type attestation:
     ~microsoft.azure.management.provisioningservices.models.AttestationMechanism
    :param iot_hub_host_name:
    :type iot_hub_host_name: str
    :param initial_twin_state:
    :type initial_twin_state:
     ~microsoft.azure.management.provisioningservices.models.TwinState
    :param etag:
    :type etag: str
    :param generation_id:
    :type generation_id: str
    :param provisioning_status: Possible values include: 'enabled', 'disabled'
    :type provisioning_status: str or
     ~microsoft.azure.management.provisioningservices.models.enum
    :param created_date_time_utc:
    :type created_date_time_utc: datetime
    :param last_updated_date_time_utc:
    :type last_updated_date_time_utc: datetime
    """

    _validation = {
        'enrollment_group_id': {'required': True},
        'attestation': {'required': True},
    }

    _attribute_map = {
        'enrollment_group_id': {'key': 'enrollmentGroupId', 'type': 'str'},
        'attestation': {'key': 'attestation', 'type': 'AttestationMechanism'},
        'iot_hub_host_name': {'key': 'iotHubHostName', 'type': 'str'},
        'initial_twin_state': {'key': 'initialTwinState', 'type': 'TwinState'},
        'etag': {'key': 'etag', 'type': 'str'},
        'generation_id': {'key': 'generationId', 'type': 'str'},
        'provisioning_status': {'key': 'provisioningStatus', 'type': 'str'},
        'created_date_time_utc': {'key': 'createdDateTimeUtc', 'type': 'iso-8601'},
        'last_updated_date_time_utc': {'key': 'lastUpdatedDateTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, enrollment_group_id, attestation, iot_hub_host_name=None, initial_twin_state=None, etag=None, generation_id=None, provisioning_status=None, created_date_time_utc=None, last_updated_date_time_utc=None):
        super(EnrollmentGroup, self).__init__()
        self.enrollment_group_id = enrollment_group_id
        self.attestation = attestation
        self.iot_hub_host_name = iot_hub_host_name
        self.initial_twin_state = initial_twin_state
        self.etag = etag
        self.generation_id = generation_id
        self.provisioning_status = provisioning_status
        self.created_date_time_utc = created_date_time_utc
        self.last_updated_date_time_utc = last_updated_date_time_utc
