from fastapi import FastAPI
from .database.db import engine, Base
from .routers import user


app = FastAPI(title="Know Your Weather API", 
              description="API that offers accurate and up-to-date weather data, helping users stay informed and prepared", 
              version="1.0.0")


Base.metadata.create_all(bind=engine)


@app.get("/v1/", tags=["Home"], description="This is the root Route of the app")
def read_root_v1():
    return {"message":"Welcome to KnowYourWeather API - version 1"}


app.include_router(user.router, prefix='/v1')