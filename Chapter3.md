Chapter 3: Variables

All values in python are objects.
As such initilising a variable in python calls a constructor (e.g. int(1) is a constructor).

All variables are pointers to an object in the heap (dynamically-allocated memory):
In Python:  int x = 5
...is the same as...
In Cpp:     int* x = new int(5);

Cannot do static memory allocation in Python.
Python variables don't have a type (the object they point to has a type).
Don't need to delete memory (handled automatically).

Classes:

Python:
    class Person:
        pass

    person = Person()

Cpp equivalent:
    class Person {};

    int main() {
    Person* person = new Person(); // classes also allocated on the heap
    delete person;
    return 0;
    }
// there exists no way to statically allocate e.g. Person person = Person()

Can do multiple simultaneous assignments:
x, y, z = 3, 9, 5
x = y = 395

Shorthand swap:
x, y = y, x
