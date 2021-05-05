from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import _backend as b

router = APIRouter(
    prefix="/html"
)

# creating an authentication mechanism for stating that we are
# currently in the application; doesn't need to be secret just needs
# to be there an available to send back to the api
authID = "okie_dokie_artichokie"


# root html endpoint
@router.get("/", response_class = HTMLResponse)
async def send_html(request: Request):
    # returning three different items:
    ##+ html template that we want to serve
    ##+ the response to the request
    ##+ the authentication password that goes along with the font-end
    return b.htmlTemplates.TemplateResponse(
        "homepage/index.html",
        {"request": request,
         "authID": authID
         }
    )