from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

htmlRouter = APIRouter(
    prefix="/html"
)

# creating an authentication mechanism for stating that we are
# currently in the application; doesn't need to be secret just needs
# to be there an available to send back to the api
authID = "okie_dokie_artichokie"

### main page HTML response
templates = Jinja2Templates(directory="./_frontend/homepage/templates")
htmlRouter.mount("/static", StaticFiles(directory="./_frontend/homepage/static"), name="static")

@htmlRouter.get("/", response_class = HTMLResponse)
async def send_html(request: Request):
    # returning three different items:
    ##+ html template that we want to serve
    ##+ the response to the request
    ##+ the authentication password that goes along with the font-end
    return templates.TemplateResponse(
        "index.html",
        {"request": request,
         "authID": authID
         }
    )