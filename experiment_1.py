from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API! Use /add?a=3&b=4 to add numbers."}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

class substractmodel(BaseModel):
    a: int
    b: int


def substract(a: int, b: int):
    return {"result": a - b}

@app.post("/substract")
def substract_numbar(data: substractmodel):
    return {"result": data.a - data.b}