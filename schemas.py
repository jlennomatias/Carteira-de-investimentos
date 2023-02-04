from pydantic import BaseModel
from typing import List


class UserCreateInput(BaseModel):
    name: str


class UserFavoriteInput(BaseModel):
    user_id: int
    codigo: str


class UserCreateOutput(BaseModel):
    message: str


class AlternativeOutput(UserCreateOutput):
    detail: str


class FavoriteList(BaseModel):
    id: int
    codigo_ativo: str
    user_id: int
    class Config:
        orm_mode = True

class UserList(BaseModel):
    id: int
    name: str
    favorites: List[FavoriteList]

    class Config:
        orm_mode = True

