from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from uuid import UUID

class TaskSubmitRequest(BaseModel):
    matrix_file_path: str = Field(..., description="Path to the adjacency matrix file")
    reference_network_path: str = Field(..., description="Path to the human reference network file")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Optional metadata for the task")

class TaskStatusResponse(BaseModel):
    task_id: UUID
    status: str = Field(..., description="Current status: PENDING, RUNNING, COMPLETED, FAILED")
    progress: float = Field(default=0.0, description="Progress from 0.0 to 1.0")
    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
