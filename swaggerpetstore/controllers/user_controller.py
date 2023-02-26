# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from swaggerpetstore.api_helper import APIHelper
from swaggerpetstore.configuration import Server
from swaggerpetstore.controllers.base_controller import BaseController
from swaggerpetstore.http.auth.o_auth_2 import OAuth2
from swaggerpetstore.models.user import User
from swaggerpetstore.exceptions.api_exception import APIException


class UserController(BaseController):

    """A Controller to access Endpoints in the swaggerpetstore API."""

    def __init__(self, config, call_back=None):
        super(UserController, self).__init__(config, call_back)

    def create_users_with_list_input(self,
                                     body):
        """Does a POST request to /user/createWithList.

        Creates list of users with given input array

        Args:
            body (list of User): List of user object

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/createWithList'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 0:
            raise APIException('successful operation', _response)
        self.validate_response(_response)

    def get_user_by_name(self,
                         username):
        """Does a GET request to /user/{username}.

        Get user by user name

        Args:
            username (string): The name that needs to be fetched. Use user1
                for testing.

        Returns:
            User: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/{username}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'username': {'value': username, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise APIException('Invalid username supplied', _response)
        elif _response.status_code == 404:
            raise APIException('User not found', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, User.from_dictionary)

        return decoded

    def update_user(self,
                    username,
                    body):
        """Does a PUT request to /user/{username}.

        This can only be done by the logged in user.

        Args:
            username (string): name that need to be updated
            body (User): Updated user object

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/{username}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'username': {'value': username, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise APIException('Invalid user supplied', _response)
        elif _response.status_code == 404:
            raise APIException('User not found', _response)
        self.validate_response(_response)

    def delete_user(self,
                    username):
        """Does a DELETE request to /user/{username}.

        This can only be done by the logged in user.

        Args:
            username (string): The name that needs to be deleted

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/{username}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'username': {'value': username, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url)
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise APIException('Invalid username supplied', _response)
        elif _response.status_code == 404:
            raise APIException('User not found', _response)
        self.validate_response(_response)

    def login_user(self,
                   username,
                   password):
        """Does a GET request to /user/login.

        Logs user into the system

        Args:
            username (string): The user name for login
            password (string): The password for login in clear text

        Returns:
            string: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/login'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'username': username,
            'password': password
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise APIException('Invalid username/password supplied', _response)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def logout_user(self):
        """Does a GET request to /user/logout.

        Logs out current logged in user session

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/logout'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 0:
            raise APIException('successful operation', _response)
        self.validate_response(_response)

    def create_users_with_array_input(self,
                                      body):
        """Does a POST request to /user/createWithArray.

        Creates list of users with given input array

        Args:
            body (list of User): List of user object

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user/createWithArray'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 0:
            raise APIException('successful operation', _response)
        self.validate_response(_response)

    def create_user(self,
                    body):
        """Does a POST request to /user.

        This can only be done by the logged in user.

        Args:
            body (User): Created user object

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 0:
            raise APIException('successful operation', _response)
        self.validate_response(_response)
