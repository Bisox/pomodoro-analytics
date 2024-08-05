from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Tasks(DeclarativeBase):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    pomodoro_count = Mapped[int]
    category_id: Mapped[int]


class Categories(DeclarativeBase):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]