from fastapi import FastAPI, Query
import uvicorn
from typing import Optional
import datetime

app = FastAPI()

@app.get("/", tags=["home"])
@app.get("/d")
def index():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.get("/query1")
def query_1(qqq):
    return qqq

@app.get("/query2")
def query_2(q: Optional[str] = Query(None, max_length=50)):
    return { "value" : q}

@app.post("/post1")
def post_1(model):
    return model

#if __name__ == "__main__":
uvicorn.run(app, port=8181)
