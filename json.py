import json

# DESERIALISATION
# Read json from file into dict/list
with open("input.json", "r") as jsonfile: 
    data = json.load(jsonfile) # data is a dict of lists

# Read json from string into dict/list
json_string = '[{"id": 2, "name": "Basilisk"}, {"id": 6, "name": "Nagaraja"}]'
datas = json.loads(json_string) # loads() is short for loadString

# SERIALISATION
# Write json from dict/list
d = {"id": 2, "name": "Basilisk"}
with open("output.json", "w") as jsonfile: 
    json.dump(d, jsonfile)

# Write json from dict/list to string
json_string = json.dumps(d) # dumps() is short for dumpString
print(json_string)
