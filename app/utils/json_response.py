from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def auth_response(status_code: int, message: str, access_token: str, token_type:str, data: Optional[dict] = None) -> JSONResponse:
    """ Returns data for successful auth login
    """
    response_data = {
        "status_code": status_code,
        "message": message,
        "access_token": access_token,
        "token_type": token_type
    }
    
    if data is not None:
        response_data["data"] = data

    return JSONResponse(status_code=status_code, content=jsonable_encoder(response_data))