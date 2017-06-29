# coding: utf-8

"""
    Wavefront Public API

    <p>Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront UI you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CloudIntegration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'force_save': 'bool',
        'name': 'str',
        'id': 'str',
        'service': 'str',
        'in_trash': 'bool',
        'additional_tags': 'dict(str, str)',
        'last_received_data_point_ms': 'int',
        'last_metric_count': 'int',
        'cloud_watch': 'CloudWatchConfiguration',
        'cloud_trail': 'CloudTrailConfiguration',
        'last_error_event': 'Event',
        'ec2': 'EC2Configuration',
        'last_error': 'str',
        'last_error_ms': 'int',
        'last_processor_id': 'str',
        'last_processing_timestamp': 'int',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'updater_id': 'str',
        'creator_id': 'str',
        'service_refresh_rate_in_mins': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'force_save': 'forceSave',
        'name': 'name',
        'id': 'id',
        'service': 'service',
        'in_trash': 'inTrash',
        'additional_tags': 'additionalTags',
        'last_received_data_point_ms': 'lastReceivedDataPointMs',
        'last_metric_count': 'lastMetricCount',
        'cloud_watch': 'cloudWatch',
        'cloud_trail': 'cloudTrail',
        'last_error_event': 'lastErrorEvent',
        'ec2': 'ec2',
        'last_error': 'lastError',
        'last_error_ms': 'lastErrorMs',
        'last_processor_id': 'lastProcessorId',
        'last_processing_timestamp': 'lastProcessingTimestamp',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId',
        'creator_id': 'creatorId',
        'service_refresh_rate_in_mins': 'serviceRefreshRateInMins',
        'deleted': 'deleted'
    }

    def __init__(self, force_save=None, name=None, id=None, service=None, in_trash=None, additional_tags=None, last_received_data_point_ms=None, last_metric_count=None, cloud_watch=None, cloud_trail=None, last_error_event=None, ec2=None, last_error=None, last_error_ms=None, last_processor_id=None, last_processing_timestamp=None, created_epoch_millis=None, updated_epoch_millis=None, updater_id=None, creator_id=None, service_refresh_rate_in_mins=None, deleted=None):
        """
        CloudIntegration - a model defined in Swagger
        """

        self._force_save = None
        self._name = None
        self._id = None
        self._service = None
        self._in_trash = None
        self._additional_tags = None
        self._last_received_data_point_ms = None
        self._last_metric_count = None
        self._cloud_watch = None
        self._cloud_trail = None
        self._last_error_event = None
        self._ec2 = None
        self._last_error = None
        self._last_error_ms = None
        self._last_processor_id = None
        self._last_processing_timestamp = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self._creator_id = None
        self._service_refresh_rate_in_mins = None
        self._deleted = None

        if force_save is not None:
          self.force_save = force_save
        if name is not None:
          self.name = name
        if id is not None:
          self.id = id
        if service is not None:
          self.service = service
        if in_trash is not None:
          self.in_trash = in_trash
        if additional_tags is not None:
          self.additional_tags = additional_tags
        if last_received_data_point_ms is not None:
          self.last_received_data_point_ms = last_received_data_point_ms
        if last_metric_count is not None:
          self.last_metric_count = last_metric_count
        if cloud_watch is not None:
          self.cloud_watch = cloud_watch
        if cloud_trail is not None:
          self.cloud_trail = cloud_trail
        if last_error_event is not None:
          self.last_error_event = last_error_event
        if ec2 is not None:
          self.ec2 = ec2
        if last_error is not None:
          self.last_error = last_error
        if last_error_ms is not None:
          self.last_error_ms = last_error_ms
        if last_processor_id is not None:
          self.last_processor_id = last_processor_id
        if last_processing_timestamp is not None:
          self.last_processing_timestamp = last_processing_timestamp
        if created_epoch_millis is not None:
          self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
          self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
          self.updater_id = updater_id
        if creator_id is not None:
          self.creator_id = creator_id
        if service_refresh_rate_in_mins is not None:
          self.service_refresh_rate_in_mins = service_refresh_rate_in_mins
        if deleted is not None:
          self.deleted = deleted

    @property
    def force_save(self):
        """
        Gets the force_save of this CloudIntegration.

        :return: The force_save of this CloudIntegration.
        :rtype: bool
        """
        return self._force_save

    @force_save.setter
    def force_save(self, force_save):
        """
        Sets the force_save of this CloudIntegration.

        :param force_save: The force_save of this CloudIntegration.
        :type: bool
        """

        self._force_save = force_save

    @property
    def name(self):
        """
        Gets the name of this CloudIntegration.
        The human-readable name of this integration

        :return: The name of this CloudIntegration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudIntegration.
        The human-readable name of this integration

        :param name: The name of this CloudIntegration.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this CloudIntegration.

        :return: The id of this CloudIntegration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudIntegration.

        :param id: The id of this CloudIntegration.
        :type: str
        """

        self._id = id

    @property
    def service(self):
        """
        Gets the service of this CloudIntegration.
        A value denoting which cloud service this integration integrates with

        :return: The service of this CloudIntegration.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this CloudIntegration.
        A value denoting which cloud service this integration integrates with

        :param service: The service of this CloudIntegration.
        :type: str
        """
        allowed_values = ["CLOUDWATCH", "CLOUDTRAIL", "EC2"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def in_trash(self):
        """
        Gets the in_trash of this CloudIntegration.

        :return: The in_trash of this CloudIntegration.
        :rtype: bool
        """
        return self._in_trash

    @in_trash.setter
    def in_trash(self, in_trash):
        """
        Sets the in_trash of this CloudIntegration.

        :param in_trash: The in_trash of this CloudIntegration.
        :type: bool
        """

        self._in_trash = in_trash

    @property
    def additional_tags(self):
        """
        Gets the additional_tags of this CloudIntegration.
        A list of point tag key-values to add to every point ingested using this integration

        :return: The additional_tags of this CloudIntegration.
        :rtype: dict(str, str)
        """
        return self._additional_tags

    @additional_tags.setter
    def additional_tags(self, additional_tags):
        """
        Sets the additional_tags of this CloudIntegration.
        A list of point tag key-values to add to every point ingested using this integration

        :param additional_tags: The additional_tags of this CloudIntegration.
        :type: dict(str, str)
        """

        self._additional_tags = additional_tags

    @property
    def last_received_data_point_ms(self):
        """
        Gets the last_received_data_point_ms of this CloudIntegration.
        Time that this integration last received a data point, in epoch millis

        :return: The last_received_data_point_ms of this CloudIntegration.
        :rtype: int
        """
        return self._last_received_data_point_ms

    @last_received_data_point_ms.setter
    def last_received_data_point_ms(self, last_received_data_point_ms):
        """
        Sets the last_received_data_point_ms of this CloudIntegration.
        Time that this integration last received a data point, in epoch millis

        :param last_received_data_point_ms: The last_received_data_point_ms of this CloudIntegration.
        :type: int
        """

        self._last_received_data_point_ms = last_received_data_point_ms

    @property
    def last_metric_count(self):
        """
        Gets the last_metric_count of this CloudIntegration.
        Number of metrics / events ingested by this integration the last time it ran

        :return: The last_metric_count of this CloudIntegration.
        :rtype: int
        """
        return self._last_metric_count

    @last_metric_count.setter
    def last_metric_count(self, last_metric_count):
        """
        Sets the last_metric_count of this CloudIntegration.
        Number of metrics / events ingested by this integration the last time it ran

        :param last_metric_count: The last_metric_count of this CloudIntegration.
        :type: int
        """

        self._last_metric_count = last_metric_count

    @property
    def cloud_watch(self):
        """
        Gets the cloud_watch of this CloudIntegration.
        CloudWatch specific configurations. Only applicable when service=CLOUDWATCH

        :return: The cloud_watch of this CloudIntegration.
        :rtype: CloudWatchConfiguration
        """
        return self._cloud_watch

    @cloud_watch.setter
    def cloud_watch(self, cloud_watch):
        """
        Sets the cloud_watch of this CloudIntegration.
        CloudWatch specific configurations. Only applicable when service=CLOUDWATCH

        :param cloud_watch: The cloud_watch of this CloudIntegration.
        :type: CloudWatchConfiguration
        """

        self._cloud_watch = cloud_watch

    @property
    def cloud_trail(self):
        """
        Gets the cloud_trail of this CloudIntegration.
        CloudTrail specific configurations. Only applicable when service=CLOUDTRAIL

        :return: The cloud_trail of this CloudIntegration.
        :rtype: CloudTrailConfiguration
        """
        return self._cloud_trail

    @cloud_trail.setter
    def cloud_trail(self, cloud_trail):
        """
        Sets the cloud_trail of this CloudIntegration.
        CloudTrail specific configurations. Only applicable when service=CLOUDTRAIL

        :param cloud_trail: The cloud_trail of this CloudIntegration.
        :type: CloudTrailConfiguration
        """

        self._cloud_trail = cloud_trail

    @property
    def last_error_event(self):
        """
        Gets the last_error_event of this CloudIntegration.

        :return: The last_error_event of this CloudIntegration.
        :rtype: Event
        """
        return self._last_error_event

    @last_error_event.setter
    def last_error_event(self, last_error_event):
        """
        Sets the last_error_event of this CloudIntegration.

        :param last_error_event: The last_error_event of this CloudIntegration.
        :type: Event
        """

        self._last_error_event = last_error_event

    @property
    def ec2(self):
        """
        Gets the ec2 of this CloudIntegration.
        EC2 specific configurations. Only applicable when service=EC2

        :return: The ec2 of this CloudIntegration.
        :rtype: EC2Configuration
        """
        return self._ec2

    @ec2.setter
    def ec2(self, ec2):
        """
        Sets the ec2 of this CloudIntegration.
        EC2 specific configurations. Only applicable when service=EC2

        :param ec2: The ec2 of this CloudIntegration.
        :type: EC2Configuration
        """

        self._ec2 = ec2

    @property
    def last_error(self):
        """
        Gets the last_error of this CloudIntegration.
        Digest of the last error encountered by Wavefront servers when fetching data using this integration

        :return: The last_error of this CloudIntegration.
        :rtype: str
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        """
        Sets the last_error of this CloudIntegration.
        Digest of the last error encountered by Wavefront servers when fetching data using this integration

        :param last_error: The last_error of this CloudIntegration.
        :type: str
        """

        self._last_error = last_error

    @property
    def last_error_ms(self):
        """
        Gets the last_error_ms of this CloudIntegration.
        Time, in epoch millis, of the last error encountered by Wavefront servers when fetching data using this integration

        :return: The last_error_ms of this CloudIntegration.
        :rtype: int
        """
        return self._last_error_ms

    @last_error_ms.setter
    def last_error_ms(self, last_error_ms):
        """
        Sets the last_error_ms of this CloudIntegration.
        Time, in epoch millis, of the last error encountered by Wavefront servers when fetching data using this integration

        :param last_error_ms: The last_error_ms of this CloudIntegration.
        :type: int
        """

        self._last_error_ms = last_error_ms

    @property
    def last_processor_id(self):
        """
        Gets the last_processor_id of this CloudIntegration.
        Opaque id of the last Wavefront integrations service to act on this integration

        :return: The last_processor_id of this CloudIntegration.
        :rtype: str
        """
        return self._last_processor_id

    @last_processor_id.setter
    def last_processor_id(self, last_processor_id):
        """
        Sets the last_processor_id of this CloudIntegration.
        Opaque id of the last Wavefront integrations service to act on this integration

        :param last_processor_id: The last_processor_id of this CloudIntegration.
        :type: str
        """

        self._last_processor_id = last_processor_id

    @property
    def last_processing_timestamp(self):
        """
        Gets the last_processing_timestamp of this CloudIntegration.
        Time, in epoch millis, that this integration was last processed

        :return: The last_processing_timestamp of this CloudIntegration.
        :rtype: int
        """
        return self._last_processing_timestamp

    @last_processing_timestamp.setter
    def last_processing_timestamp(self, last_processing_timestamp):
        """
        Sets the last_processing_timestamp of this CloudIntegration.
        Time, in epoch millis, that this integration was last processed

        :param last_processing_timestamp: The last_processing_timestamp of this CloudIntegration.
        :type: int
        """

        self._last_processing_timestamp = last_processing_timestamp

    @property
    def created_epoch_millis(self):
        """
        Gets the created_epoch_millis of this CloudIntegration.

        :return: The created_epoch_millis of this CloudIntegration.
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """
        Sets the created_epoch_millis of this CloudIntegration.

        :param created_epoch_millis: The created_epoch_millis of this CloudIntegration.
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """
        Gets the updated_epoch_millis of this CloudIntegration.

        :return: The updated_epoch_millis of this CloudIntegration.
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """
        Sets the updated_epoch_millis of this CloudIntegration.

        :param updated_epoch_millis: The updated_epoch_millis of this CloudIntegration.
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """
        Gets the updater_id of this CloudIntegration.

        :return: The updater_id of this CloudIntegration.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """
        Sets the updater_id of this CloudIntegration.

        :param updater_id: The updater_id of this CloudIntegration.
        :type: str
        """

        self._updater_id = updater_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this CloudIntegration.

        :return: The creator_id of this CloudIntegration.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this CloudIntegration.

        :param creator_id: The creator_id of this CloudIntegration.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def service_refresh_rate_in_mins(self):
        """
        Gets the service_refresh_rate_in_mins of this CloudIntegration.
        Service refresh rate in minutes.

        :return: The service_refresh_rate_in_mins of this CloudIntegration.
        :rtype: int
        """
        return self._service_refresh_rate_in_mins

    @service_refresh_rate_in_mins.setter
    def service_refresh_rate_in_mins(self, service_refresh_rate_in_mins):
        """
        Sets the service_refresh_rate_in_mins of this CloudIntegration.
        Service refresh rate in minutes.

        :param service_refresh_rate_in_mins: The service_refresh_rate_in_mins of this CloudIntegration.
        :type: int
        """

        self._service_refresh_rate_in_mins = service_refresh_rate_in_mins

    @property
    def deleted(self):
        """
        Gets the deleted of this CloudIntegration.

        :return: The deleted of this CloudIntegration.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this CloudIntegration.

        :param deleted: The deleted of this CloudIntegration.
        :type: bool
        """

        self._deleted = deleted

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CloudIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
