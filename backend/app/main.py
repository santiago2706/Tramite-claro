from fastapi import FastAPI
from app.core.settings import settings
from app.api.routers.health import router_health

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)
app.include_router(router_health)

@app.get("/")
def root ():
    return {
        "project": settings.app_name,
        "enviroment": settings.app_env,
        "version": settings.app_version,
        "status": "running"
    }
