# Make string formatting more readable
name = "Josiah"
count = 10
possession = "cars"
print(f"{name} has {count} {possession}")

# More control over how to format strings
pi = 3.141592653589793
print(f"PI with three significant digits: {pi:.3}")
print(f"PI with three decimal points: {pi:.3f}")
print(f"PI with three significant digits, 9-character width is {pi:9.3}")
print(f"PI with three significant digits, 9-character width padded with 0 is {pi:09.3}")

# Escaping strings
print('the boy\'s mother') # like Cpp
# for readability, prefer to enclose with different type quote
print("the boy's mother")
print('''the boy's mother''')
print('he said, "hello"')
