from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# declaring the api as app
app = FastAPI()

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

@app.get("/html/", response_class=HTMLResponse)
async def send_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
