#!/usr/bin/env python3
""" base_models - Contains BaseModel which defines
common attributes and methods of all the objects
"""
import uuid
from datetime import datetime


class BaseModel:
    ''' BaseModel - Base class
    Defines all common attributes and methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        ''' Initialize public instance attributes &
        Deserializes a dictionary rep of an instance to an instance
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        ''' Updates updated_at attribute
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns a dictionary containing all key/values pairs of
        __dict__ of an instance
        '''
        data = self.__dict__.copy()

        # Convert datetime objects to iso strings
        for key in ['created_at', 'updated_at']:
            if isinstance(data.get(key), datetime):
                data[key] = data.get(key).isoformat()

        data['__class__'] = self.__class__.__name__

        return data

    def __str__(self):
        ''' Returns an informal/readable string representation of
        an instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
