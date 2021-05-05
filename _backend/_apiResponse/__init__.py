from fastapi import APIRouter

apiRouter = APIRouter(
    prefix="/api"
)


### root api call
@apiRouter.get("/")
async def root():
    return {"message": "Hello there!",
            "response" : {
                "status": 200,
                "message": "okay"
                }
            }