#!/usr/bin/env python3
""" Serialize instances to JSON file &
Deserializes JSON to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# class registry
CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


class FileStorage:
    ''' FileStorage - Storage Engine to serialize instance to JSON &
    Deserialize JSON to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Sets in __objects the object obj
        '''
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        ''' Serializes __objects to JSON file __filepath
        '''
        with open(FileStorage.__file_path, 'w') as json_file:
            dumpable_dict = {
                    key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()
                    }
            json.dump(dumpable_dict, json_file)

    def reload(self):
        ''' Deserializes the JSON file to __objects
        '''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, obj_dict in data.items():
                    class_name = obj_dict.get('__class__')
                    cls = CLASSES.get(class_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**obj_dict)
