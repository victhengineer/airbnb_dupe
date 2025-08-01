#!/usr/bin/env pytthon3
""" Tests for Place Model
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceModel(unittest.TestCase):
    ''' Place Model Test Case
    '''
    def test_place_is_basemodel_subclass(self):
        ''' Test that place is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_has_all_attributes(self):
        ''' Test that place has all attributes as required
        '''
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_place_city_id_is_string(self):
        ''' Test That Place city_id is a string
        '''
        self.assertTrue(isinstance(Place.city_id, str))

    def test_place_user_id_is_string(self):
        ''' Test that Place user_id is a string
        '''
        self.assertTrue(isinstance(Place.user_id, str))

    def test_place_name_is_string(self):
        ''' Test that Place name is a string
        '''
        self.assertTrue(isinstance(Place.name, str))

    def test_place_description_is_string(self):
        ''' Test that Place description is a string
        '''
        self.assertTrue(isinstance(Place.description, str))

    def test_place_number_rooms_is_integer(self):
        ''' Test that Place number_rooms is an integer
        '''
        self.assertTrue(isinstance(Place.number_rooms, int))

    def test_place_max_guest_is_integer(self):
        ''' Test that Place max_guest attribute is an integer
        '''
        self.assertTrue(isinstance(Place.max_guest, int))

    def test_place_price_by_night_is_integer(self):
        ''' Test that Place price_by_night attribute is an integer
        '''
        self.assertTrue(isinstance(Place.price_by_night, int))

    def test_place_latitude_is_float(self):
        ''' Test that Place latitude attribute is a float
        '''
        self.assertTrue(isinstance(Place.latitude, float))

    def test_place_longitude_is_float(self):
        ''' Test that Place longitude attribute is a float
        '''
        self.assertTrue(isinstance(Place.longitude, float))

    def test_amenity_ids_is_list(self):
        ''' Test that Place amenity_ids attribute is a list
        '''
        self.assertTrue(isinstance(Place.amenity_ids, list))

