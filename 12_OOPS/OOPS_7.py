"""self attributes (Instance attributes)

Definition:
Attributes that belong to a specific object (instance) of a class.

Syntax:
Defined inside methods using self, usually inside init.

Example:
"""
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

"""
Usage:
Each object can have its own unique values for these attributes.
"""

car1 = Car("Red", "Tesla")
car2 = Car("Blue", "BMW")

print(car1.color)   # Red
print(car2.color)   # Blue

"""
When to use:

When the value should be different for each object.
When the data is specific to that instance.

Class attributes

Definition:
Attributes that are shared across all instances of a class.

Syntax:
Defined directly inside the class, not inside any method.

Example:
"""

class Car:
    wheels = 4      # class attribute

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

"""
Usage:
All objects share the same value, unless you override it for a specific instance.
"""
car1 = Car("Red", "Tesla")
car2 = Car("Blue", "BMW")

print(car1.wheels)   # 4
print(car2.wheels)   # 4

Car.wheels = 6       # change class attribute for all instances

print(car1.wheels)   # 6
print(car2.wheels)   # 6

"""
When to use:

When the value should be common to all objects.

Example: constants, counters, or configuration shared across all instances.
"""


class Dog:
    species = "Canine"   # class attribute

    def __init__(self, name, age):
        self.name = name     # instance attribute
        self.age = age       # instance attribute

dog1 = Dog("Bruno", 3)
dog2 = Dog("Rocky", 5)

print(dog1.species)   # Canine
print(dog2.species)   # Canine

Dog.species = "Domestic Canine"  # affects all dogs
print(dog1.species)   # Domestic Canine

dog1.age = 4   # only affects dog1
print(dog1.age, dog2.age)  # 4, 5

"""
In short:
Use self attributes when the value should vary for each object.
Use class attributes when the value should be shared by all objects of the class.
"""