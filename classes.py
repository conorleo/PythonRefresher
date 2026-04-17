class Person:
    def __init__(self, name, age, nationality="uk"): # constructor (always needs self as the first parameter, equivalent to this pointer in C++)
        self.name = name # instance attribute (unique to each instance of the class)
        self.age = age                      # public attribute (attributes are public by default, opposite to Cpp)
        self.__nationality = nationality    # private attribute (prepend with double underscore to convert from an attribute (public) to a property (private), can only be accessed within the class, not even by subclasses)
        self._salary = 35000                # protected attribute (prepend with single underscore to indicate that it is intended for internal use, but not enforced by the language, can be accessed by subclasses)

    def introduce_self(self): # method (also needs self as the first parameter, even if doesn't need any attributes)
        print(f"Hey man! Name's {self.name}, from {self.__nationality}!")

    def emigrate(self, new_country): # effectively a setter (see below for recommended way to do this with @property)
        self.__nationality = new_country

manager = Person("John Doe", 30, "usa") # creating a new object in the heap (in the background calls Person.__new__()) and invoking the constructor
print(manager) # prints the memory address of the object, since we haven't defined a __str__ method for the class

manager.introduce_self()
manager.emigrate("canada") # python automatically converts this to Person.emigrate(manager, "canada"). The way shown is more readable
manager._Person__nationality = "canada" # can also access private attribute by name mangling, but not recommended
manager.introduce_self()

## Overloading dunder methods
class Vector: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __add__(self, other): 
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self): 
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2) 
v2 = Vector(5, 7) 
v3 = v1 + v2 # python automatically recognises this as our overloaded __add__ method
print(v3) # python invokes our overloaded __str__ method to print the vector in a readable format instead of the default memory address


## Inheritance
# all classes in Python 3 are subclasses of object by default
class Employee(Person): # Employee inherits from Person, so has all the same attributes and methods as Person
    def __init__(self):
        super().__init__("John Doe", 30) # call the constructor of the parent class to initialise the inherited attributes
        self.employee_id = "00-01-30"


## Encapsulation with @property decorator
# Getting and setting non-public properties.
class Country:
    def __init__(self, nationality="uk"): # constructor (always needs self as the first parameter, equivalent to this pointer in C++)
        self.__nationality = nationality # private attribute (prepend with double underscore to convert from an attribute (public) to a property (private), can only be accessed within the class, not even by subclasses)

    @property # decorator converts nationality from private property to public readable attribute
    def nationality(self): # getter
        return self.__nationality
    
    @nationality.setter # decorator converts nationality from a private property to a public writeable attribute
    def nationality(self, new_country): # setter
        self.__nationality = new_country

nation = Country()
print(nation.nationality) # calls the getter method
nation.nationality = "usa" # calls the setter method
print(nation.nationality)


## Class Methods (equivalent to a static method in Cpp)
# Method that acts on properties whose value is shared by all instances of the class.
class France(Country):
    count = 0 # class attribute (shared by all instances of the class, same as a static variable in Cpp)
    PI = 3.14 # useful for defining constants (in CAPS)

    def __init__(self):
        super().__init__("french")
        self.drink = "wine" # instance attribute (unique to each instance of the class)
        France.count += 1 # increment the population count every time a new instance of France is created

    @classmethod # class method decorator: equivalent to a static method in Cpp
    def get_population(cls): # takes the class, cls as the first parameter instead of the instance, self
        return f"Population: {cls.count}" # does not have access to any instance attributes, only class attributes

francais = France()
print(France.get_population())
print(francais.get_population())    # deduces that francais is an instance of France and calls the class method on the class, not the instance
                                    # it doesn't matter whether we call it on the class or the instance, it will give the same result

## Static Methods (not the same as a static method in Cpp)
# Method that does not have access to the instance or class attributes but exists in the scope of the class.
class Ireland(Country):
    def __init__(self):
        super().__init__("irish")

    @staticmethod # static method decorator: does not take self or cls as the first parameter, just a regular function defined in the scope of the class
    def greet():
        print("Hello from Ireland!")

## Abstract Base Classes (ABCs)
# Class that cannot be instantiated and is intended only to be subclassed.
from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_off(self):
        pass

class Radio(Device):
    def turn_off(self):
        print("Turning off the radio. Done!")

# device = Device("Some device") # will error
radio = Radio("My radio")
radio.turn_off() # valid


## Type Hinting
# Although Python is a dynamically typed language, we can use type hints to indicate the expected 
# types of variables, function parameters and return values. This can help with code readability and debugging, 
# and can be checked with static type checkers like mypy (will flag unexpected types).
def greet(username: str, visits: int = 0) -> str: # returns str
    return f"Greetings, {username}. You have visited us {visits} times."


## Named Tuples
# A subclass of tuples that allows for named fields, making the code more readable and self-documenting.
# Can be used instead of a class when we just want to group together some related data without needing methods or mutability.
from collections import namedtuple
Coordinates = namedtuple("Coordinates", "row col")
position = Coordinates(4, 5)
print(position.row) # can access the fields by name
print(position[0])  # and as regular tuple


## Data Classes
# Shorthand for creating classes, with automatically generated __init__, __repr__, __eq__ and other methods based on the class attributes.
from dataclasses import dataclass

class Person:
    def __init__(self, name, age=0): 
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def greet(self):
        print(f"Hi! My name is {self.name}!")

# Same as above but less verbose
@dataclass
class Person:
    name: str
    age: int = 0 

    def greet(self):
        print(f"Hi! My name is {self.name}!")

lecturer = Person("Josiah", 20)
