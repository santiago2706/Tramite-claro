from fastapi import APIRouter, Depends
from app.services.health_services import HealthService
from app.api.dependencies import get_health_service

router = APIRouter()

@router.get("/health")
def health_check(
    service: HealthService = Depends(get_health_service)
):
    return service.get_status()