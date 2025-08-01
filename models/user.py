#!/usr/bin/env python3
""" Application's User Model
"""
from .base_model import BaseModel


class User(BaseModel):
    ''' User Model to handle user data in the app
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

