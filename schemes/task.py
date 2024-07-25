from pydantic import BaseModel, model_validator, ValidationError, Field


class Stask(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int  # = Field(exclude=True)

    @model_validator(mode='after')  # для выполнения пользовательских проверок на уровне модели.
    def check_name_and_pomodoro_count(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValidationError('Name and pomodoro count cannot be None')
        return self
