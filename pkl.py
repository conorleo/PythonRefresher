import pickle

courses = {
   70053: {"lecturer": "Josiah Wang", "title": "Python Programming"}, 
   70051: {"lecturer": "Robert Craven", "title": "Symbolic AI"}
}

# Serialise (pickle)
with open("output.pkl", "wb") as file: # open file in binary write mode
    pickle.dump(courses, file)

# Deserialise (unpickle)
with open("output.pkl", "rb") as file: # open file in binary read mode
    data = pickle.load(file)

print(data)
print(data == courses) # True, the deserialised data is the same as the original data
