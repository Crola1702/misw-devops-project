from sqlalchemy.orm import Session
from .base_command import BaseCommand
from src.models.blacklist_email import BlacklistEmail

class AddEmailToBlacklistCommand(BaseCommand):
    def __init__(self, db: Session, email: str, app_uuid: str, blocked_reason: str, ip_address: str):
        self.db = db
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip_address = ip_address

    def execute(self):
        blacklist_email = BlacklistEmail(
            email=self.email,
            app_uuid=self.app_uuid,
            blocked_reason=self.blocked_reason,
            ip_address=self.ip_address
        )

        self.db.add(blacklist_email)
        self.db.commit()
        self.db.refresh(blacklist_email)
        return blacklist_email
