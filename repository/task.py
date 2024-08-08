from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.database import get_db



class TaskRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session






