from fastapi import FastAPI

from app.routes.metrics import router as metrics_router
from app.routes.user_check import router as user_check_router

app = FastAPI()


app.include_router(user_check_router, prefix="/check")
app.include_router(metrics_router)
