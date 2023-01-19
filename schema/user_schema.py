from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    """create schema for user information"""
    idusers: int#Optional[BaseModel]
    usersName: str
    usersAge: int
    usersDPT: str


class DataUser(BaseModel):
    """creates schema for users update information"""
    idusers: str
    usersDPT: str
    # user_password: str