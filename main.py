from fastapi import FastAPI
from db import SessionDep


app = FastAPI()


@app.get("/")
async def ping():
    return {"pong"}
