import time

# USE SETS FOR STORING/QUERYING UNIQUE ELEMENTS WHERE ORDER IS NOT IMPORTANT

vowels = {"i", "o", "a", "a", "e", "u", "e", "i", "a"} # defined with {}
print(vowels) # prints unique elements only, order is not guaranteed

words = ["let", "it", "go", ",", "let", "it", "go", ",", "can't", "hold", "it", "back", "any", "more", "!"]
vocabulary = set(words) # can convert lists or tuples to sets

# empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

empty_dict = {} # don't mistake this for an empty set, this is an empty dictionary
print(type(empty_dict)) # dict

# Sets are useful for querying for unique element values 
# (since they are fast to parse, becuase elements are stored and retrieved by hashing)
numbers = range(1000000)

number_list = list(numbers)
start_time = time.time()
print(51232422 in number_list)
end_time = time.time()
print(f"list took {end_time - start_time:.9f} seconds")

number_set = set(numbers)
start_time = time.time()
print(51232422 in number_set)
end_time = time.time()
print(f"set took {end_time - start_time:.9f} seconds")
