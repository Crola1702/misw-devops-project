import uuid
from datetime import datetime
from pydantic import BaseModel, IPvAnyAddress

class BlacklistEmailSchemaBase(BaseModel):
    class Config:
        from_attributes = True

class BlacklistEmailPostIn(BlacklistEmailSchemaBase):
    email: str
    app_uuid: uuid.UUID
    blocked_reason: str

class BlacklistEmailPostOut(BlacklistEmailSchemaBase):
    email: str
    app_uuid: uuid.UUID
    blocked_reason: str
    ip_address: IPvAnyAddress
    createdAt: datetime

class BlacklistEmailGetOut(BlacklistEmailSchemaBase):
    is_present: bool
    blocked_reason: str
