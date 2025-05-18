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