#!/usr/bin/env python3
""" Tests for City Model
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityModel(unittest.TestCase):
    ''' City Model Test Case
    '''
    def test_city_is_basemodel_subclass(self):
        ''' Test that city is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_has_all_attributes(self):
        ''' Test that City has all the required attributes
        '''
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))

    def test_city_state_id_is_string(self):
        ''' Test that City state_id attribute is a string
        '''
        self.assertTrue(isinstance(City.state_id, str))

    def test_city_name_is_string(self):
        ''' Test that City name attribute is a string
        '''
        self.assertTrue(isinstance(City.name, str))

