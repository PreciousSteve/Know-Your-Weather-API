from fastapi import FastAPI


app = FastAPI(title="Know Your Weather API", 
              description="API that offers accurate and up-to-date weather data, helping users stay informed and prepared", 
              version="1.0.0")


@app.get("/v1/", tags=["Home"], description="This is the root Route of the app")
def read_root_v1():
    return {"message":"Welcome to KnowYourWeather API - version 1"}