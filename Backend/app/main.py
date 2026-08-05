from fastapi import FastAPI

from app.routers.audit import router as audit_router


app = FastAPI(
    title="GEO Auditor API",
    description="AI-powered Generative Engine Optimization Auditor",
    version="1.0.0"
)


@app.get("/")
async def health_check():
    return {
        "success": True,
        "message": "GEO Auditor API is running 🚀"
    }


app.include_router(
    audit_router,
    prefix="/api/v1",
    tags=["Audit"]
)