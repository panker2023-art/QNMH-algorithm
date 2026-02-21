import asyncio
from concurrent.futures import ProcessPoolExecutor
from typing import Callable, Any, Dict
from uuid import UUID, uuid4

class TaskManager:
    """Manages asynchronous computation tasks."""

    def __init__(self, max_workers: int = 4):
        self.executor = ProcessPoolExecutor(max_workers=max_workers)
        self.tasks: Dict[UUID, Dict[str, Any]] = {}

    async def submit_task(self, func: Callable, *args, **kwargs) -> UUID:
        """Submit a CPU-bound task to the process pool."""
        task_id = uuid4()
        self.tasks[task_id] = {
            "status": "PENDING",
            "progress": 0.0,
            "result": None,
            "error_message": None
        }

        # Run task in executor without blocking the event loop
        loop = asyncio.get_running_loop()
        future = loop.run_in_executor(self.executor, func, *args, **kwargs)
        
        # Add callback to update status when finished
        asyncio.create_task(self._monitor_task(task_id, future))
        
        return task_id

    async def _monitor_task(self, task_id: UUID, future: asyncio.Future):
        """Monitor task completion and update state."""
        self.tasks[task_id]["status"] = "RUNNING"
        try:
            result = await future
            self.tasks[task_id]["status"] = "COMPLETED"
            self.tasks[task_id]["progress"] = 1.0
            self.tasks[task_id]["result"] = result
        except Exception as e:
            self.tasks[task_id]["status"] = "FAILED"
            self.tasks[task_id]["error_message"] = str(e)

    def get_task_status(self, task_id: UUID) -> Dict[str, Any]:
        """Retrieve task status."""
        if task_id not in self.tasks:
            return {"status": "NOT_FOUND"}
        return self.tasks[task_id]

# Singleton instance for the API
task_manager = TaskManager()
