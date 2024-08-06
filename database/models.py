from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Tasks(Base):
    __tablename__ = 'tasks_pomodoro'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    pomodoro_count = Mapped[int]
    category_id: Mapped[int]


class Categories(Base):
    __tablename__ = 'Categories_pomodoro'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]