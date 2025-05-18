from fastapi import FastAPI

app = FastAPI()

@app.get("/") #App Decorator that defines the path for the http get method
def root():
    return {"Hello":"World"}

