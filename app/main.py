from fastapi import FastAPI


app = FastAPI(title="Know Your Weather API", 
              description="API that offers accurate and up-to-date weather data, helping users stay informed and prepared", 
              version="1.0.0")


@app.get("/", tags=["Home"], description="This is the root Route of the app")
def read_root():
    return {"message":"Welcome to KnowYourWeather API"}