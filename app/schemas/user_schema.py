from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Any

class UserCreate(BaseModel):
    username: str = Field(max_length=12)
    email: EmailStr
    password: str
    confirm_password : str
    
    @field_validator('password')
    def validate_password(cls, value:str) -> str:
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(c.islower() for c in value):
            raise ValueError('Password must contain at least 1 lowercase letter')
        if not any(c.isupper() for c in value):
            raise ValueError('Password must contain at least 1 uppercase letter')
        if not any(c.isdigit() for c in value):
            raise ValueError('Password must contain at least 1 digit')
        if not any(c in '!@#$%^&*()-_+=' for c in value):
            raise ValueError('Password ust contain at least 1 special character')
        return value
    
    @field_validator('confirm_password')
    def password_match(cls, value:str, info: Any) -> str:
        if 'password' in info.data and value != info.data['password']:
            raise ValueError('Password and Confirm password do not match')
        return value
    
    class Config:
        orm_mode = True