#!/usr/bin/env python3
""" Tests for Amenity Model
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityModel(unittest.TestCase):
    ''' Amenity Data Model Test Case
    '''
    def test_amenity_is_basemodel_subclass(self):
        ''' Test that Amenity is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_has_all_attributes(self):
        ''' Test that Amenity contains all required attributes
        '''
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_amenity_name_is_string(self):
        ''' Test that Amenity name is a string
        '''
        self.assertTrue(isinstance(Amenity.name, str))

