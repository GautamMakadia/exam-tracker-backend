from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware
from router import records, collection


app = FastAPI()
mime_excel = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

app.include_router(records.router)
app.include_router(collection.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def hello():
    return {
        "msg": "this is atmiya exam tracker api"
    }
