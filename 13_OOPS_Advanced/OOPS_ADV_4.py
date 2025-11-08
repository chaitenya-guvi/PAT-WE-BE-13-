"""
Polymorphism

A key principle in OOP is the idea of polymorphism -
an object can take on many (poly) forms (morph).

While a formal definition of polymorphism is more difficult,
 here are two important practical applications:
"""

print(len("Hello"))     # Output: 5 → works on string
print(len([1, 2, 3]))   # Output: 3 → works on list
print(len({"a": 1, "b": 2}))  # Output: 2 → works on dict


"""
Exmple 1
 The same class method works in a similar way for different classes

Each subclass will have a different implementation of the method.
If the method is not implemented in the subclass,
    the version in the parent class is called instead.

Cat.speak()  # meow
Dog.speak()  # woof
Human.speak()  # yo
"""

class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())



"""
Exmple 2 
2. The same operation works for different kinds of objects
"""
sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

print(len(sample_list))
print(len(sample_tuple))
print(len(sample_string))