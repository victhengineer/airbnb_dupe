#!/usr/bin/env python3
""" The Review Model
"""
from .base_model import BaseModel


class Review(BaseModel):
    '''Review Data Model
    '''
    place_id = ''
    user_id = ''
    text = ''
