from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.api.endpoints import router as analysis_router
from src.api.endpoints import ui_router

app = FastAPI(
    title="Quantitative Network Motif Homology (QNMH) API",
    description="Backend for QNMH algorithm and PRI evaluation system",
    version="0.1.0"
)

# Include API routers
app.include_router(analysis_router)
app.include_router(ui_router)

# Mount static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def serve_ui():
    """Serve the main UI dashboard."""
    return FileResponse("src/static/index.html")

@app.get("/health")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "version": "0.1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
