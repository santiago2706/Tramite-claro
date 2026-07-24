from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {
        "project": "Trámite Claro",
        "status": "running",
        "version": "0.1.0",
        "environment": "development",
    }
@app.get("/health")
def health_check(): 
    return {
        "status": "ok"
    }