from fastapi import APIRouter, HTTPException, BackgroundTasks, File, UploadFile
from fastapi.responses import JSONResponse
from uuid import UUID
import os
import shutil
import logging
from src.core.models.api_models import TaskSubmitRequest, TaskStatusResponse
from src.infrastructure.compute.manager import task_manager
from src.infrastructure.compute.tasks import run_qnmh_analysis

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/analysis", tags=["analysis"])
ui_router = APIRouter(prefix="/api", tags=["ui"])

UPLOAD_DIR = "src/uploads"

@ui_router.post("/upload")
async def upload_files(source_file: UploadFile = File(...), ref_file: UploadFile = File(...)):
    """
    Handle file uploads from the UI.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    source_path = os.path.join(UPLOAD_DIR, source_file.filename)
    ref_path = os.path.join(UPLOAD_DIR, ref_file.filename)
    
    with open(source_path, "wb") as buffer:
        shutil.copyfileobj(source_file.file, buffer)
        
    with open(ref_path, "wb") as buffer:
        shutil.copyfileobj(ref_file.file, buffer)
        
    return JSONResponse({
        "source_path": source_path,
        "ref_path": ref_path
    })

@router.post("/qnmh", response_model=TaskStatusResponse, status_code=202)
async def submit_qnmh_task(request: TaskSubmitRequest, background_tasks: BackgroundTasks):
    """
    Submit a new QNMH analysis task asynchronously.
    Returns immediately with a task_id for polling status.
    """
    try:
        task_id = await task_manager.submit_task(
            run_qnmh_analysis,
            matrix_file_path=request.matrix_file_path,
            reference_network_path=request.reference_network_path,
            metadata=request.metadata
        )
        
        # Initial status response
        status_info = task_manager.get_task_status(task_id)
        
        return TaskStatusResponse(
            task_id=task_id,
            status=status_info.get("status", "PENDING"),
            progress=status_info.get("progress", 0.0)
        )
    except Exception as e:
        logger.error(f"Error submitting QNMH task: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/qnmh/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: UUID):
    """
    Poll the status of a specific QNMH analysis task by ID.
    """
    status_info = task_manager.get_task_status(task_id)
    
    if status_info.get("status") == "NOT_FOUND":
        raise HTTPException(status_code=404, detail="Task not found")
        
    return TaskStatusResponse(
        task_id=task_id,
        status=status_info.get("status"),
        progress=status_info.get("progress", 0.0),
        result=status_info.get("result"),
        error_message=status_info.get("error_message")
    )
