Chapter 8: OOP

Consider if a dict (struct) can be used before using a class.

Magic/Dunder Methods: functions flanked by double underscores (__), which do special things
e.g.    constructor __init__()
        heap memory allocation __new__()
        print specified name when calling print(obj) __str__()
        __add__(), __sub__(), __mul__(), __truediv__(), __pow__() will overload their respective mathematical operators e.g. x+y actually invokes x.__add__(y)
        overloading boolean operators __lt__(), __le__(), __gt__(), __ge__(), __eq__(), __ne__() (<, <=, >, >=, ==, !=)
        Collections:
            __len__() (len(x) invokes x.__len__())
            __contains__() (item in x invokes x.__contains__(item))
            __getitem__() (x[key] invokes x.__getitem__(key))
            __setitem__() (x[key] = item invokes x.__setitem__(key, item))
            __iter__() is used to allow the class instance to be used in for loops


Keep attributes public unless there is a good reason to do otherwise (in which case use decorators to write getters and setters).
Attributes are public in a class by default (not the same as in Cpp where they are private by default).

Class Methods (equivalent to static methods in Cpp)
- A class method is bound to the class and not to the class instance.
- Does not have access to the attributes of the instance, only the attributes of the class

Static Methods (not the same as static methods in Cpp)
- A regular function defined in the scope of a class that does not have access to the class's attributes
