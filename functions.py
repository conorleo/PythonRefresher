def do_something(a, b, c=2, d="great", e=5, f="john", g="python", h=-1, i=0, j=[]): # default params (only first two require args in this example)
    print(f"{a}; {b}; {c}; {d}; {e}; {f}; {g}; {h}; {i}; {j}")
    return None # no return statement will implicitly return None

x = do_something("first", "second", i=2, f="josiah") # can use keyword arguments to avoid entering optional params in order (also more readable)
                                                     # a,b are positional args - required (in order)
                                                     # the rest are keyword args - optional (in any order)

# Anything in python is an object, including function so they can be assigned to variables:
my_func = do_something
print(type(my_func)) # class 'function'
# Hence can pass function as an arg to another function:
def laugh():
    print("MUAHAHAHAHA!! :D")

def cry():
    print("WAAA!! TT_TT")      

def multiplier(func, repeats):
    for i in range(repeats):
        func()

multiplier(laugh, 5)
multiplier(cry, 2)

## Pass variable number of positional args:
def enroll(*courses): # use *before param to pack the params into a tuple
    print(type(courses))  # <class 'tuple'>
    for course in courses: 
        print(course)

enroll("Probabilistic Inference", "Introduction to Machine Learning",
    "Computer Vision", "Graphics")

## Pass variable number of keyword args:
def customise_page(**kwargs): # use **before param to pack the params into a dict
    print(type(kwargs)) # <class 'dict'>
    parse_args(kwargs)

# define defaults in another function
def parse_args(options):
    for key, value in options.items():
        if key == "background":
            #set_background(value)
            pass
        elif key == "width":
            #set_width(value)
            pass
        elif key == "avatar":
            #set_avatar(value)
            pass
        else:
            print(f"Unknown keyword {key}.")
            return
        
customise_page(background="red", width=500, avatar="selfie.jpg")
