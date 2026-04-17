# Hypertext Transfer Protocol
Application-level protocol for distributed, collaborative, hypermedia info systems

Defines how a client (e.g. browser) should communicate with a server (e.g. Google).
Client sends a HTTP request to the server. Server processes it and sends a HTTP response back to the client.

## HTTP Request
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0 

request line: GET is the request method, retrieving the resource /index.html
request header: host is a compulsory header to point to the server
an optional request header: this indicates to the server what browser the client is using
message body: optional, not included here

## HTTP Response
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 155
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"
Accept-Ranges: bytes
Connection: close

<html>
  <head>
    <title>An Example Page</title>
  </head>
  <body>
    <p>Hello World, this is a very simple HTML document.</p>
  </body>
</html>

status line: status code 200 (successful) and ok. Other HTTP status codes include: "404" (Not found), "403" (Forbidden), "500" (Internal Server Error), "503" (Service Unavailable)
response header: expect response to be html code, etc...
message body: optional, in this case the html source code itself.

## API
Application Programming Interface
A defined set of functions a server has provided for a client to call. 

# Web API
The web address is the endpoint of a web API.

# REST API
REpresentational State Transfer
An architectural style for web services that follow these principles that define how HTTP should be used, which makes them RESTful APIs (if not strictly conforming they are called REST-like APIs):
- Client and servers are separate.
- Statelessness: each request is independent of others so each request must contain everything needed to understand the request.
- Cacheability: Resources (the thing you receive from a GET call) allow caching.
- Layered system.
- Uniform interface.

REST API responses usually JSON, text or XML.
REST APIs are a special subset of Web APIs.
In REST APIs the item received from GET is called a resource.

# Common Requests
- GET: read/retreive a resource from the server
- POST: create a resource on the server
- PUT: update an existing resource on the server
- DELETE: remove an existing resource on the server

# Web Frameworks
For hosting web servers:
- Django
- Flask
- FastAPI (quickly dominating)
