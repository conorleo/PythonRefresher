# USE DICTS FOR CREATING NESTED STRUCTS OR FAST LOOKUPS

# Creating
my_dict = {"name": "Alice", "age": 30, "city": "New York"} # from scratch
student_dict = dict([("00-01-30", "Ali"), ("00-02-11", "Simon"), ("00-05-67", "Francesca"), ("00-09-88", "Cho")]) # from list of tuple pairs
student_dict = {} # from empty
student_dict["00-01-30"] = "Ali"
student_dict["00-02-11"] = "Simon"
student_dict["00-05-67"] = "Francesca"
student_dict["00-09-88"] = "Cho"

# Retrieving
if "00-11-22" in student_dict: # good practice to check if key exists before trying to retrieve value by key to prevent error
    student = student_dict["00-02-11"] # using key to get value
student = student_dict.get("00-09-88", "John Doe") # get method allows you to specify a default value if key is not found, instead of throwing an error

# Use as nested structs
student = {
            "name": "Josiah", 
            "id": "00-02-11", 
            "degree": "MSc Computing",
            "courses": [
                {
                    "title": "Introduction to Machine Learning", 
                    "code": "60012"
                },
                { 
                    "title": "Computer Vision",
                    "code": "60006"
                }
            ]
          }
