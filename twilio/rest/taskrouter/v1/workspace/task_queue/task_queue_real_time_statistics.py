# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TaskQueueRealTimeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        """
        super(TaskQueueRealTimeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    def get(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __call__(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsList>'


class TaskQueueRealTimeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the TaskQueueRealTimeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsPage
        """
        super(TaskQueueRealTimeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskQueueRealTimeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        return TaskQueueRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsPage>'


class TaskQueueRealTimeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        super(TaskQueueRealTimeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics'.format(**self._solution)

    def fetch(self, task_channel=values.unset):
        """
        Fetch a TaskQueueRealTimeStatisticsInstance

        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.

        :returns: Fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        params = values.of({'TaskChannel': task_channel, })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskQueueRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsContext {}>'.format(context)


class TaskQueueRealTimeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueRealTimeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        super(TaskQueueRealTimeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'activity_statistics': payload['activity_statistics'],
            'longest_task_waiting_age': deserialize.integer(payload['longest_task_waiting_age']),
            'longest_task_waiting_sid': payload['longest_task_waiting_sid'],
            'task_queue_sid': payload['task_queue_sid'],
            'tasks_by_priority': payload['tasks_by_priority'],
            'tasks_by_status': payload['tasks_by_status'],
            'total_available_workers': deserialize.integer(payload['total_available_workers']),
            'total_eligible_workers': deserialize.integer(payload['total_eligible_workers']),
            'total_tasks': deserialize.integer(payload['total_tasks']),
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TaskQueueRealTimeStatisticsContext for this TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = TaskQueueRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_queue_sid=self._solution['task_queue_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def activity_statistics(self):
        """
        :returns: The current Worker status count breakdown by Activity
        :rtype: dict
        """
        return self._properties['activity_statistics']

    @property
    def longest_task_waiting_age(self):
        """
        :returns: The age of the longest waiting Task
        :rtype: unicode
        """
        return self._properties['longest_task_waiting_age']

    @property
    def longest_task_waiting_sid(self):
        """
        :returns: The SID of the longest waiting Task
        :rtype: unicode
        """
        return self._properties['longest_task_waiting_sid']

    @property
    def task_queue_sid(self):
        """
        :returns: The task_queue_sid
        :rtype: unicode
        """
        return self._properties['task_queue_sid']

    @property
    def tasks_by_priority(self):
        """
        :returns: The Tasks broken down by priority
        :rtype: dict
        """
        return self._properties['tasks_by_priority']

    @property
    def tasks_by_status(self):
        """
        :returns: The Tasks broken down by status
        :rtype: dict
        """
        return self._properties['tasks_by_status']

    @property
    def total_available_workers(self):
        """
        :returns: The total number of Workers available for Tasks in this TaskQueue
        :rtype: unicode
        """
        return self._properties['total_available_workers']

    @property
    def total_eligible_workers(self):
        """
        :returns: The total number of Workers eligible for Tasks in this TaskQueue, irrespective of Activity state.
        :rtype: unicode
        """
        return self._properties['total_eligible_workers']

    @property
    def total_tasks(self):
        """
        :returns: The total number of Tasks
        :rtype: unicode
        """
        return self._properties['total_tasks']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, task_channel=values.unset):
        """
        Fetch a TaskQueueRealTimeStatisticsInstance

        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.

        :returns: Fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        return self._proxy.fetch(task_channel=task_channel, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsInstance {}>'.format(context)
