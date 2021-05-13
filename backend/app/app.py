from typing import Optional
from fastapi import FastAPI
from config import Config

app = FastAPI()


@app.route("/")
def hello_world():
    return "<p>HELLO</p>"
