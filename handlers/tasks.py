from fastapi import APIRouter, status

from schemes.task import Stask


router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.get("/all",
            response_model=list[Stask])
async def get_tasks():
    return task


@router.post("/add",
             response_model=Stask)
async def create_task(task: Stask):
    return task


@router.patch("/{task_id}",
              response_model=Stask)
async def update_task(task_id: int, name: str):
    ...



@router.delete("/{task_id}",
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    ...