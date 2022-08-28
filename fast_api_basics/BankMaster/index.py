from fastapi import FastAPI
from routes.index import bankmaster
app = FastAPI()


app.include_router(bankmaster)
