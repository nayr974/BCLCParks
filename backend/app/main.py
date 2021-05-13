from typing import Optional
from fastapi import FastAPI
from .config import Config

from fastapi_sqlalchemy import DBSessionMiddleware

app: FastAPI = FastAPI()

# add middlewares
app.add_middleware(DBSessionMiddleware, db_url=Config.DB_URL)

@app.route("/")
def hello_world():
    return "<p>HELLO</p>"
