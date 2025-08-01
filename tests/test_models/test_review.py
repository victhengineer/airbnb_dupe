#!/usr/bin/env python3
""" Tests for Review Model
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewModel(unittest.TestCase):
    ''' Review Model Test Case
    '''
    def test_review_is_basemodel_subclass(self):
        ''' Test that review is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_has_all_attributes(self):
        ''' Test that Review has all required attributes
        '''
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_review_place_id_is_string(self):
        ''' Test that Review place_id is a string
        '''
        self.assertTrue(isinstance(Review.place_id, str))

    def test_review_user_id_is_string(self):
        ''' Test that Review user_id is a string
        '''
        self.assertTrue(isinstance(Review.user_id, str))

    def test_review_text_is_string(self):
        ''' Test tha review text is a string
        '''
        self.assertTrue(isinstance(Review.text, str))

