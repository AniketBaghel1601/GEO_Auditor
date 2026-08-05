from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.audit import router as audit_router


app = FastAPI(
    title="GEO Auditor API",
    description="AI-powered Generative Engine Optimization Auditor",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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