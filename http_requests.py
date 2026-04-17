import requests #  for very high-level (human-readable) HTTP requests
import json

# GET: read/retrieve data from a server

# 1) Access Web Server: receive the html file hosted on a server
response = requests.get("http://www.doc.ic.ac.uk")
# help(response) # print methods of response object
print(response.status_code) # successful
print(response.headers) # Get the response headers
print(response.headers["Content-Type"]) # Get the value of a specific header, in this case the content type of the response
print(response.text) # The message body HTML source code of the webpage

# 2) # Access Web API: receive the output of an API endpoint in JSON format
response = requests.get("https://randomuser.me/api")
print(json.loads(response.content))

response = requests.get("https://randomuser.me/api/?gender=female") # can add parameters to URL
print(json.loads(response.content))

response = requests.get("https://randomuser.me/api", params={"gender": "female"}) # can add parameters separately as a dict
print(json.loads(response.content))

# POST: create a new resource on the server
new_article = {"author": "Python", "title": "Yes we can", "content": 4}
response = requests.post("http://localhost:5000/articles", data=new_article) # cannot pass resource in URL, must be in message body (data)
print(response.json()) # print json as dict

# PUT: update an existing resource on the server
updated_article = {"title": "We love snake puns"}
response = requests.put("http://localhost:5000/articles/4", data=updated_article) # id 4
print(response.json())

# DELETE: delete an existing resource on the server
response = requests.delete("http://localhost:5000/articles/4")
print(response.json())


# Authentication
username = "cobra"
password = "python"
response = requests.get("http://localhost:5000/secret", auth=(username, password)) # HTTP Basic Authenticaltion (simplest method for Web APIs): pass username and password as a tuple to the auth parameter
print(response.json())                                                             # lumps the user and pass in an Authorization header in the HTTP request

# Sessions
with requests.Session() as session:
    username = "cobra"
    password = "hiss"
    session.auth = (username, password)
    first_response = session.get("http://localhost:5000/greeting") # don't need to specify auth for each HTTP request
    second_response = session.get("http://localhost:5000/greeting") # memory is acheived by the server passing cookies back to the client (which will be included in the clients next request by default)
    third_response = session.get("http://localhost:5000/greeting")  # some argue that cookies breaks the statelessness of RESTful APIs (requests no longer independent)

