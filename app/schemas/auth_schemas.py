from typing import Optional
from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    password: str
    invite_token: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    role: str