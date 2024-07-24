from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.post('/{task_id}')
async def add_task(task_id):
    return {'added': task_id}


@router.get('/')
async def get_task():
    return []