#!/usr/bin/env python3
""" Tests for User Model
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserModel(unittest.TestCase):
    ''' User Model test cases
    '''
    def test_user_is_basemodel_subclass(self):
        ''' Test that User inherits from BaseModel
        '''
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_has_all_attr(self):
        ''' Test that user has all required attributes
        '''
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_email_is_string(self):
        ''' Test that email is a string
        '''
        self.assertTrue(isinstance(User.email, str))

    def test_password_is_string(self):
        ''' Test that password is a  string
        '''
        self.assertTrue(isinstance(User.password, str))

    def test_first_name_is_string(self):
        ''' Test that first name is a string
        '''
        self.assertTrue(isinstance(User.first_name, str))

    def test_last_name_is_string(self):
        ''' Test that last name is a string
        '''
        self.assertTrue(isinstance(User.last_name, str))

