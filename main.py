from fastapi import FastAPI, Depends

from city_crud_api.router import city_router, get_db

app = FastAPI()


@app.get("/")
def hello():
    return "Hello!"

app.include_router(city_router, dependencies=[Depends(get_db)])

