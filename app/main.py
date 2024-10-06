from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from .database.db import engine, Base
from .routers import register
from .utils.error_handlers import (integrity_error_handler, general_exception_handler, http_exception_handler, validation_exception_handler)


app = FastAPI(title="Know Your Weather API", 
              description="API that offers accurate and up-to-date weather data, helping users stay informed and prepared", 
              version="1.0.0")


Base.metadata.create_all(bind=engine)


@app.get("/v1/", tags=["Home"], description="This is the root Route of the app")
def read_root_v1():
    return {"message":"Welcome to KnowYourWeather API - version 1"}


app.include_router(register.router, prefix='/v1')



# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, general_exception_handler)