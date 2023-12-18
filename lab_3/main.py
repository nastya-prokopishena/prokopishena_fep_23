from fastapi import FastAPI, APIRouter
from api import app as api_app

app = FastAPI()

router = APIRouter()

router.include_router(api_app, prefix="/api")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
