from fastapi import FastAPI
from ._apiResponse import apiRouter
from ._htmlResponse import htmlRouter

# declaring the api as app
app = FastAPI()

# including the modular routers
app.include_router(apiRouter)
app.include_router(htmlRouter)
