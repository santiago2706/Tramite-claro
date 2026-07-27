from fastapi import APIRouter
router = APIRoouter()

@router.get("/health")
def health_check(): 
    return {
        "status": "ok"
    }