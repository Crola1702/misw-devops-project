# import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from .database import Base
# from sqlalchemy.dialects.postgresql import UUID


class BlacklistEmail(Base):
    __tablename__ = "blacklist"

    email = Column(String, primary_key=True, index=True)
    app_uuid = Column(String)
    blocked_reason = Column(String(255))
    ip_address = Column(String)
    createdAt = Column(DateTime)

    def __init__(self, email, app_uuid, blocked_reason, ip_address):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip_address = ip_address
        self.createdAt = datetime.now()
