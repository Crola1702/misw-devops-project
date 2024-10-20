from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.errors.errors import ApiError
from src.blueprints.blacklist_router import router
from src.models.database import Base, engine
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.exception_handler(ApiError)
async def api_error_handler(_: Request, exc: ApiError):
    return JSONResponse(
        status_code=exc.code,
        content={"msg": exc.description},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"msg": "Invalid request body"},
    )

@app.get("/")
async def root():
    return {"message": "Blacklist service is running"}
