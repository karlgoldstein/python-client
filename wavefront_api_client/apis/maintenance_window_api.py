# coding: utf-8

"""
    Wavefront Public API

    <p>Wavefront public APIs enable you to interact with Wavefront servers using standard web service API tools. You can use the APIs to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront UI you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class MaintenanceWindowApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_maintenance_window(self, **kwargs):
        """
        Create a maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_maintenance_window(async=True)
        >>> result = thread.get()

        :param async bool
        :param MaintenanceWindow body: Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre>
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_maintenance_window_with_http_info(**kwargs)
        else:
            (data) = self.create_maintenance_window_with_http_info(**kwargs)
            return data

    def create_maintenance_window_with_http_info(self, **kwargs):
        """
        Create a maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_maintenance_window_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param MaintenanceWindow body: Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre>
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_maintenance_window" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/api/v2/maintenancewindow', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseContainerMaintenanceWindow',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_maintenance_window(self, id, **kwargs):
        """
        Delete a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_maintenance_window(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_maintenance_window_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_maintenance_window_with_http_info(id, **kwargs)
            return data

    def delete_maintenance_window_with_http_info(self, id, **kwargs):
        """
        Delete a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_maintenance_window_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_maintenance_window" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_maintenance_window`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/api/v2/maintenancewindow/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseContainerMaintenanceWindow',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_maintenance_window(self, **kwargs):
        """
        Get all maintenance windows for a customer
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_maintenance_window(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_maintenance_window_with_http_info(**kwargs)
        else:
            (data) = self.get_all_maintenance_window_with_http_info(**kwargs)
            return data

    def get_all_maintenance_window_with_http_info(self, **kwargs):
        """
        Get all maintenance windows for a customer
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_maintenance_window_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_maintenance_window" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/api/v2/maintenancewindow', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseContainerPagedMaintenanceWindow',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_maintenance_window(self, id, **kwargs):
        """
        Get a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_maintenance_window(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_maintenance_window_with_http_info(id, **kwargs)
        else:
            (data) = self.get_maintenance_window_with_http_info(id, **kwargs)
            return data

    def get_maintenance_window_with_http_info(self, id, **kwargs):
        """
        Get a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_maintenance_window_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_maintenance_window" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_maintenance_window`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/api/v2/maintenancewindow/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseContainerMaintenanceWindow',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_maintenance_window(self, id, **kwargs):
        """
        Update a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_maintenance_window(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param MaintenanceWindow body: Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre>
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_maintenance_window_with_http_info(id, **kwargs)
        else:
            (data) = self.update_maintenance_window_with_http_info(id, **kwargs)
            return data

    def update_maintenance_window_with_http_info(self, id, **kwargs):
        """
        Update a specific maintenance window
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_maintenance_window_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param MaintenanceWindow body: Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre>
        :return: ResponseContainerMaintenanceWindow
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_maintenance_window" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_maintenance_window`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api('/api/v2/maintenancewindow/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseContainerMaintenanceWindow',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
