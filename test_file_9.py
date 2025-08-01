#!/usr/bin/env python3
from models import storage
from models.review import Review

all_objs = storage.all()
print("-- Reloaded Objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create Review --")
my_review = Review()
my_review.place_id = 'uuid4-123'
my_review.user_id = 'user1-uuid'
my_review.text = "Top tier Hospitality"
my_review.save()
print(my_review)
