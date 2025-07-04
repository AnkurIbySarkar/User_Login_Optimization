from fastapi import APIRouter
from pydantic import BaseModel

from app.metrics.cache_tracker import get_metrics, reset_metrics


class MetricsResponse(BaseModel):
    hits: int
    misses: int


class ResetResponse(BaseModel):
    message: str


router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/cache", response_model=MetricsResponse)
def read_cache_metrics():
    return get_metrics()


@router.delete("/cache/reset", response_model=ResetResponse)
def reset_cache_metrics():
    reset_metrics()
    return {"message": "Cache metrics reset"}
