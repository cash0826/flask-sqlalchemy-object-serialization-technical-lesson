# lib/serialize.py
from marshmallow import Schema, fields
from pprint import pprint

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
        
    def give_treat(self):
        self.tail_wagging = True
        
    def scold(self):
        self.tail_wagging = False
    
# schema. Fields can be omitted if needed, for example private info
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()

# dog = Dog(name="Snuggles", breed="Beagle", tail_wagging=True)

dogs = [
    Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
    Dog(name="Wags", breed="Collie", tail_wagging=False)
]

pprint(DogSchema(many=True).dumps(dogs))

# Fields can be limited during instance too, using "only" parameter. 
# Default is Schema()

# dog_schema = DogSchema(only=("name", "breed"))

# Fields can be excluded.
# Expects a list of strings, make sure to include a comma

# dog_schema = DogSchema(exclude=("breed",))

# dumps() can be called upon initialization like so:
# dog_dict = DogSchema(only=("breed","name")).dumps()

# dog_dict = dog_schema.dumps(dog)
# pprint(dog_dict)

