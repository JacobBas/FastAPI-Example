from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# declaring the api as app
app = FastAPI()

# creating an authentication mechanism for stating that we are
# currently in the application; doesn't need to be secret just needs
# to be there an available to send back to the api
authID = "okie_dokie_artichokie"


# JSON REST API ===============================================================
### root api call
@app.get("/")
async def root():
    return {"message": "Hello there!",
            "response" : {
                "status": 200,
                "message": "okay"
                }
            }


# HTML RESPONSES ==============================================================
### main page HTML response
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/html/", response_class = HTMLResponse)
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
