#!/usr/bin/env python3
from models import storage
from models.place import Place


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create Place --")
my_place = Place()
my_place.city_id = '1234-uui4-uu12'
my_place.user_id = 'user1-uuid-uuid4'
my_place.name = 'Comfy XO'
my_place.description = 'Best You Can Get'
my_place.number_rooms = 2
my_place.number_bathrooms = 2
my_place.max_guest = 7
my_place.price_by_night = 8000
my_place.latitude = 1.200988867564
my_place.longitude = 2.45609876578
my_place.amenity_ids = ['Amenity1-uuid', 'Amen3-uuid']
my_place.save()
print(my_place)
