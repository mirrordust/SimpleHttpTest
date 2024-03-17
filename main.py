from typing import Union

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/header")
async def header(user_agent: Annotated[Union[str, None], Header()] = None,
                 host: Annotated[Union[str, None], Header()] = None):
    return {
        "user_agent": user_agent,
        "host": host,
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
