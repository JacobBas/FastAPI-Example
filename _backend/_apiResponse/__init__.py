from fastapi import APIRouter

router = APIRouter(
    prefix="/api"
)

### root api call
@router.get("/")
async def root():
    return {"message": "Hello there!",
            "response" : {
                "status": 200,
                "message": "okay"
                }
            }