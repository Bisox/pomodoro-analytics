from pydantic import BaseModel


class Stask(BaseModel):
    id: int
    name: str
    pomodoro_count: int
    category_id: int