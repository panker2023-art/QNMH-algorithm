from fastapi import FastAPI
from src.api.endpoints import router as analysis_router

app = FastAPI(
    title="Jitian Intelligence API",
    description="Backend for QNMH algorithm and PRI evaluation system",
    version="0.1.0"
)

app.include_router(analysis_router)

@app.get("/health")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "version": "0.1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
