from sqlalchemy.orm import Session
from .base_command import BaseCommand
from src.models.blacklist_email import BlacklistEmail

class GetBlacklistEmailCommand(BaseCommand):
    def __init__(self, db: Session, email: str):
        self.db = db
        self.email = email

    def execute(self):
        email_data = self.db.query(BlacklistEmail).filter(BlacklistEmail.email == self.email).first()
        return email_data