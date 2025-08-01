#!/usr/bin/env python3
""" Tests for State Data Model
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateModel(unittest.TestCase):
    ''' State Model Test Case
    '''
    def test_state_is_basemodel_subclass(self):
        ''' Test that State is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_has_all_attributes(self):
        ''' Test that State has all the required attributes
        '''
        self.assertTrue(hasattr(State, 'name'))

    def test_state_name_is_string(self):
        ''' Test that State name is a string as required
        '''
        self.assertTrue(isinstance(State.name, str))
