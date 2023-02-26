# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from swaggerpetstore.decorators import lazy_property
from swaggerpetstore.configuration import Configuration
from swaggerpetstore.configuration import Environment
from swaggerpetstore.controllers.pet_controller import PetController
from swaggerpetstore.controllers.store_controller import StoreController
from swaggerpetstore.controllers.user_controller import UserController


class SwaggerpetstoreClient(object):

    @lazy_property
    def pet(self):
        return PetController(self.config)

    @lazy_property
    def store(self):
        return StoreController(self.config)

    @lazy_property
    def user(self):
        return UserController(self.config)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, timeout=60,
                 max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION,
                 o_auth_client_id='TODO: Replace',
                 o_auth_redirect_uri='TODO: Replace', config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         o_auth_client_id=o_auth_client_id,
                                         o_auth_redirect_uri=o_auth_redirect_uri)
        else:
            self.config = config
