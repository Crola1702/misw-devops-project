from typing import Annotated
from fastapi import APIRouter, Depends, Header, status, Request
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from src.errors.errors import NotAuthorizedError, InvalidTokenError
from src.commands.add_email_to_blacklist import AddEmailToBlacklistCommand
from src.commands.get_blacklist_email import GetBlacklistEmailCommand
from src.commands.reset_database import ResetDatabaseCommand
from src.models.schemas import BlacklistEmailPostOut, BlacklistEmailPostIn, BlacklistEmailGetOut
from src.models.database import get_db

router = APIRouter()

def verify_authorization(authorization: Annotated[str | None, Header()]):
    if authorization is None:
        raise NotAuthorizedError
    if not authorization.startswith("Bearer "):
        raise InvalidTokenError
    return authorization


@router.get("/ping")
async def ping():
    return PlainTextResponse("pong")

@router.post("/reset")
async def reset(db: Session = Depends(get_db)):
    ResetDatabaseCommand(db).execute()
    return {"msg": "Todos los datos fueron eliminados"}

@router.post("/blacklists", status_code=status.HTTP_201_CREATED, response_model=BlacklistEmailPostOut)
def create_post(body: BlacklistEmailPostIn, request: Request, db: Session = Depends(get_db), authorization: Annotated[str | None, Header()] = None):
    verify_authorization(authorization)
    client_host = request.client.host
    print(f"Client host: {client_host}")
    command = AddEmailToBlacklistCommand(db, body.email, str(body.app_uuid), body.blocked_reason, client_host)
    return command.execute()

@router.get("/blacklists/{email}", response_model=BlacklistEmailGetOut)
def get_post(email: str, db: Session = Depends(get_db), authorization: Annotated[str | None, Header()] = None):
    verify_authorization(authorization)
    command = GetBlacklistEmailCommand(db, email)
    email_data = command.execute()
    if email_data is None:
        return {"is_present": False, "blocked_reason": ""}
    return {"is_present": True, "blocked_reason": email_data.blocked_reason}
