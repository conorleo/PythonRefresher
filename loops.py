# looping over list
words = ["let", "it", "go", ",", "let", "it", "go", ",", "can't", "hold", "it", "back", "any", "more", "!"]
for word in words: # loop over elements
    print(word)
for (word, index) in enumerate(words, 0): # loop over elements and indices simultaneosuly with enumerate(), optional 2nd arg to indicate index to start counting from (default = 0)
    print(f"{index}: {word}")

# looping over dict
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person: # loop over keys
    print(person[key])
for (key, value) in person.items(): # loop over keys and values simultaneosuly with .items()
    print(f"{key} is {value}")

# loop over two lists in simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for (name, age) in zip(names, ages): # alternate between elements in list1 and list2, with zip()
    print(f"{name} is {age} years old")
