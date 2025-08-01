#!/usr/bin/env python3
from models import storage
from models.city import City
from models.state import State

all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create new city --")
my_city = City()
my_city.state_id = '1234-uuid-uuid4'
my_city.name = 'Houstin'
my_city.save()
print(my_city)
