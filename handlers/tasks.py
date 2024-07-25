from fastapi import APIRouter, status

from fixtures import tasks
from schemes.task import Stask


router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/all",
            response_model=list[Stask])
async def get_all_tasks():
    return tasks


@router.post("/add",
             response_model=Stask)
async def create_task(task: Stask):
    tasks.append(task)
    return task


@router.patch("/{task_id}",
              response_model=Stask)
async def update_task(task_id: int, name: str):
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = name
            return task


@router.delete("/{task_id}",
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.pop(tasks.index(task))
            return task
    return {"message": "Task not found"}