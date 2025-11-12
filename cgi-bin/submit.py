#!/usr/bin/env python3
"""
cgi-bin/submit.py
-----------------
This is the classic Python CGI script version of the form handler.

It works when running a local web server via:
    python3 -m http.server 8080 --cgi

It demonstrates how form data can be sent to a Python program 
using GET or POST, which then prints back HTML as output.

File type: Python (.py)
Used here for backward compatibility and to teach basic web scripting.
"""
import cgi
import os

print("Content-Type: text/html\n")

# Parse the incoming form data
form = cgi.FieldStorage()

# Detect the request method (GET or POST)
method = os.environ.get("REQUEST_METHOD", "UNKNOWN")

# Retrieve parameters
name = form.getvalue("name")
city = form.getvalue("city")

# Conditional logic for GET vs POST
if method == "POST" and name:
    message = f"Hello, {name}! (sent via POST)"
elif method == "GET" and city:
    message = f"Ah, you're from {city}! (sent via GET)"
else:
    message = "No valid data received."

# Send HTML back
print(f"""
<!DOCTYPE html>
<html>
  <head><title>Response</title></head>
  <body>
    <h1>{message}</h1>
    <p>Request method: {method}</p>
    <a href="/index.html">Go back</a>
  </body>
</html>
""")

#we have to run this locally to mock up the GET POST functionality:
# first we make it an executable file:
#chmod +x cgi-bin/submit.py
#then we launch a localhost which is like a local instance of a web server:
# python3 -m http.server 8080 --cgi


