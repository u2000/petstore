# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerpetstore.models.category import Category
from swaggerpetstore.models.tag import Tag


class Pet(object):

    """Implementation of the 'Pet' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        category (Category): TODO: type description here.
        name (string): TODO: type description here.
        photo_urls (list of string): TODO: type description here.
        tags (list of Tag): TODO: type description here.
        status (StatusEnum): pet status in the store

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "photo_urls": 'photoUrls',
        "id": 'id',
        "category": 'category',
        "tags": 'tags',
        "status": 'status'
    }

    def __init__(self,
                 name=None,
                 photo_urls=None,
                 id=None,
                 category=None,
                 tags=None,
                 status=None):
        """Constructor for the Pet class"""

        # Initialize members of the class
        self.id = id
        self.category = category
        self.name = name
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get('name')
        photo_urls = dictionary.get('photoUrls')
        id = dictionary.get('id')
        category = Category.from_dictionary(dictionary.get('category')) if dictionary.get('category') else None
        tags = None
        if dictionary.get('tags') is not None:
            tags = [Tag.from_dictionary(x) for x in dictionary.get('tags')]
        status = dictionary.get('status')

        # Return an object of this model
        return cls(name,
                   photo_urls,
                   id,
                   category,
                   tags,
                   status)
