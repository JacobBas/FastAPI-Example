from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# declaring the api as app
app = FastAPI()

# html index files
htmlTemplates = Jinja2Templates(directory="./_frontend")

# static css and javascript files
app.mount("/homepage/static", StaticFiles(directory="./_frontend"), name="static")

# importing the routers to the api and html responses
import _backend._apiResponse as api
import _backend._htmlResponse as html

# including the modular routers
app.include_router(api.router)
app.include_router(html.router)