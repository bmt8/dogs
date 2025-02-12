from enum import Enum

class AnimalType(Enum):
    DOG = 1
    CAT = 2
    SQUIRREL = 3

class Animal:
    pass

class Dog(Animal):
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        super().__init__()
