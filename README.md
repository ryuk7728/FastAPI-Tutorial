# FastAPI-Tutorial
Tutorial for FastAPI

FastAPI is a web framework that helps us build API apps with Python

Its async(non sequential) in nature which makes it fast, efficient and scalable.


uvicorn helloWorld:app --reload (helloWorld->file name, app->app name and reload will make app auto refresh anytime there's changes to the file)

Eg. of routes:
/abc,/xyz


curl (short for Client URL) is a command-line tool used to transfer data to or from a server using various protocols like HTTP, HTTPS, FTP, and more.

It’s widely used for testing APIs, downloading files, or interacting with web servers without needing a browser.


Curl Request Used for testing ToDo.py: curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=work'

-X POST -> Specifies the http method i.e post request
-H "Content-Type: application/json" -> Indicates that json data is being sent (We arent sending JSON via -d in this case)
http://127.0.0.1:8000/items?item=work -> URL being called where we're passing the parameter item with value "work as a query parameter"

For sending multiple parameters: http://127.0.0.1:8000/items?item=work&item1=play 

For Error Handling: 

We can return a HTTP response status code in case of error which is standardized in nature.
Eg. for item not found we can return 404 Not Found

FastAPI supports Pydantic models which allows you to structure your data and provide additional validation


JSON type curl request:

curl -X POST -H 'Content-Type: application/json' -d '{"text":"melon"}' http://127.0.0.1:8000/items

-d -> Indicates the JSON Payload

Another Eg:

curl -X POST -H 'Content-Type: application/json' -d '{"text":"strawberry","is_done":"true"}' 'http://127.0.0.1:8000/items'


Validating response:

This can be included in the function prototype: 'response_model=list[Item]', 

✅ Purpose of response_model=list[Item]:
It tells FastAPI that the response returned by this endpoint will be a list of Item objects, and it should:

🧠 What it does:
✅ Filter output: Only include the fields defined in the Item model, even if your internal items list has more fields.

✅ Validate response: Ensures the returned data matches the structure of a list of Item.

✅ Auto-generate OpenAPI docs: Your /docs (Swagger UI) will show exactly what the endpoint returns.

✅ Improves clarity: Makes your API self-documenting and safer, especially for frontend/backend integration.

Interactive documentation for testing: 
http://127.0.0.1:8000/docs#

FastAPI Advantages:

Async by default
Easier to use

Disadvantages:
Less adoption and support compared to Flask