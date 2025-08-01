#!/usr/bin/env python3
""" Test Module to test Base Model
"""
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch


class TestBaseModelId(unittest.TestCase):
    ''' TestBaseModel - A Test Case to test BaseModel ID attribute
    '''
    def setUp(self):
        '''Sets Up for a test
        '''
        with patch('models.storage.new'):
            self.test_model = BaseModel()

    def tearDown(self):
        ''' Tidies up after every test
        '''
        del self.test_model

    def test_constructor_does_not_fail(self):
        ''' Test that the constructor __init__ does not fail
        '''
        try:
            with patch('models.storage.new'):
                test_model_1 = BaseModel()
        except Exception as e:
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
        ids = set()
        with patch('models.storage.new'):
            for _ in range(1000):
                with self.subTest(i=_):
                    self.assertNotIn(BaseModel().id, ids)
                    ids.add(BaseModel().id)


# BaseModel Timestamps Tests
class TestBaseModelTimestamps(unittest.TestCase):
    ''' TestBaseModelTimestamps - Test Case to test timestamps of BaseModel
    '''
    def setUp(self):
        ''' setUp - Sets Up before every test
        '''
        with patch('models.storage.new'):
            self.test_model = BaseModel()

    def tearDown(self):
        ''' tearDown - Tidies up after every test
        '''
        del self.test_model

    def test_timestamps_are_not_none(self):
        ''' Test that timestamps are not None
        '''
        self.assertIsNotNone(self.test_model.created_at)
        self.assertIsNotNone(self.test_model.updated_at)

    def test_created_at_is_datetime(self):
        ''' Test that created_at is an instance of datetime
        '''
        self.assertIsInstance(self.test_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        ''' Test that updated_at is an instance of datetime
        '''
        self.assertIsInstance(self.test_model.updated_at, datetime)

    def test_created_equals_updated_initially(self):
        ''' Test that created_at and update_at are equal initially
        '''
        self.assertEqual(
                self.test_model.created_at,
                self.test_model.updated_at
                )

    @patch('models.storage.save')
    def test_update_at_changes_on_update(self, mock_save):
        ''' Test that update changes when an instance is updated
        '''
        self.test_model.save()
        self.assertGreater(
                self.test_model.updated_at,
                self.test_model.created_at
                )


# BaseModel Serialization Tests
class TestBaseModelSerializationToDict(unittest.TestCase):
    ''' Test instance serialization to a dictionary
    '''
    def setUp(self):
        ''' Set Up variables required by a test
        '''
        self.test_model = BaseModel()
        self.test_model_dict = self.test_model.to_dict()

    def tearDown(self):
        ''' Tidies up after every test
        '''
        del self.test_model
        del self.test_model_dict

    def test_to_dict_returns_dict(self):
        ''' Test to_dict method returns a dictionary
        '''
        self.assertIsInstance(self.test_model_dict, dict)

    def test_dict_has_all_attributes(self):
        ''' Test that the dictionary returned has all required attributes
        '''
        self.assertIn('id', self.test_model_dict)
        self.assertIn('created_at', self.test_model_dict)
        self.assertIn('updated_at', self.test_model_dict)
        self.assertIn('__class__', self.test_model_dict)

    def test_timestamps_are_strings(self):
        ''' Test that timestamps are casted to strings in the dictionary
        '''
        self.assertIsInstance(self.test_model_dict.get('created_at'), str)
        self.assertIsInstance(self.test_model_dict.get('updated_at'), str)

    def test_timestamps_are_iso_format(self):
        ''' Test that timestamps are in iso format strings
        '''
        try:
            datetime.fromisoformat(self.test_model_dict.get('created_at'))
            datetime.fromisoformat(self.test_model_dict.get('updated_at'))
        except ValueError:
            self.fail('Timestamps are not in ISO format')

    def test_custom_attributes_are_serialized(self):
        ''' Test that custom attributes are serialized
        '''
        self.test_model.name = "My Model"
        dict_obj = self.test_model.to_dict()
        self.assertIn('name', dict_obj)
        self.assertEqual(dict_obj.get('name'), 'My Model')


# Base Class Deserialization Test
class TestBaseModelDeserializationFromDict(unittest.TestCase):
    ''' Test Base Class Deserialization logics
    '''
    def setUp(self):
        ''' setUp - Sets up before every test
        '''
        self.test_model = BaseModel()
        self.test_model.name = 'Test Model'
        self.test_obj = self.test_model.to_dict()
        self.new_test_model = BaseModel(**self.test_obj)

    def tearDown(self):
        ''' tearDown - Tidies up after a test
        '''
        del self.test_model
        del self.test_obj
        del self.new_test_model

    def test_class_key_is_ignored(self):
        ''' Test that __class__ is ignored in deserialization
        '''
        self.assertFalse('__class__' in self.new_test_model.__dict__)

    def test_timestamps_converted_datetime(self):
        ''' Test that timestamps are converted to datetime from iso strings
        '''
        self.assertTrue(isinstance(self.new_test_model.created_at, datetime))
        self.assertTrue(isinstance(self.new_test_model.updated_at, datetime))
