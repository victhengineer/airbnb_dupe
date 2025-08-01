#!/usr/bin/env python3
from models import storage
from models.amenity import Amenity

all_objs = storage.all()
print('-- Reloaded objects --')
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print('-- Create a new amenity --')
my_amenity = Amenity()
my_amenity.name = "Medicare"
my_amenity.save()
print(my_amenity)
