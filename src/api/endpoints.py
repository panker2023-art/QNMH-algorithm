from fastapi import APIRouter, HTTPException, BackgroundTasks
from uuid import UUID
from src.core.models.api_models import TaskSubmitRequest, TaskStatusResponse
from src.infrastructure.compute.manager import task_manager
from src.infrastructure.compute.tasks import run_qnmh_analysis
import asyncio

router = APIRouter(prefix="/analysis", tags=["analysis"])

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
