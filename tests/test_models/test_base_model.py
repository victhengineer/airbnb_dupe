#!/usr/bin/env python3
""" Test Module to test Base Model
"""
import uuid
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' TestBaseModel - A Test Case to test BaseModel
    '''
    def setUp(self):
        ''' Runs once everytime before a test
        Sets Up for a test
        '''
        self.test_model = BaseModel()

    def test_constructor_does_not_fail(self):
        ''' Test that the constructor __init__ does not fail
        '''
        try:
            test_model_1 = BaseModel()
        except Exeption as e:
            self.fail(f"Constructor raised an exeption: {e}")

    def test_id_is_not_none(self):
        ''' Test that ID is not None
        '''
        self.assertIsNotNone(self.test_model.id)

    def test_id_is_a_string(self):
        ''' Test that ID is an instance of string
        '''
        self.assertIsInstance(self.test_model.id, str)

    def test_id_is_valid_uuid(self):
        ''' Test that ID is a valid uuid
        '''
        try:
            uuid_obj = uuid.UUID(self.test_model.id)
        except ValueError:
            self.fail('ID is not a valid UUID')

    def test_ids_are_unique(self):
        ''' Test that generated IDs are unique
        '''
        ids = {BaseModel().id for _ in range(1000)}
        self.assertEqual(len(ids), 1000)

