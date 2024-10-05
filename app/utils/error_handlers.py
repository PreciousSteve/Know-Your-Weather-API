from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

async def http_exception_handler(request: Request, exc: HTTPException):
    """HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": False,
            "status_code": exc.status_code,
            "message": exc.detail,
        },
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Validation exception handler"""
    errors = [
        {"field": error["loc"][-1], "message": error["msg"]}
        for error in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "status": False,
            "status_code": 422,
            "message": "Invalid input",
            "errors": errors,
        },
    )

async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Integrity error exception handler"""
    return JSONResponse(
        status_code=400,
        content={
            "status": False,
            "status_code": 400,
            "message": f"An unexpected error occurred: {exc}",
        },
    )

async def general_exception_handler(request: Request, exc: Exception):
    """General exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "status": False,
            "status_code": 500,
            "message": f"An unexpected error occurred: {exc}",
        },
    )