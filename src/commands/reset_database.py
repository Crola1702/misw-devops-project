from sqlalchemy.orm import Session
from src.models.blacklist_email import BlacklistEmail
from .base_command import BaseCommand

class ResetDatabaseCommand(BaseCommand):
    def __init__(self, db: Session):
        self.db = db

    def execute(self):
        deleted_rows = self.db.query(BlacklistEmail).delete()
        self.db.commit()
        print(f"{deleted_rows} rows deleted")
