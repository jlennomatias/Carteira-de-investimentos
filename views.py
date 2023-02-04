from asyncio import gather
from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService, AssetService
from schemas import UserCreateInput, UserCreateOutput, AlternativeOutput, UserFavoriteInput, UserList, FavoriteList
from typing import List


user_router = APIRouter(prefix='/user', tags=["User"])
assets_router = APIRouter(prefix='/assets', tags=["Assets"])


@user_router.post('/create', response_model=UserCreateOutput, responses={418: {"model": AlternativeOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return UserCreateOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/delete{user_id}', response_model=UserCreateOutput, responses={418: {"model": AlternativeOutput}})
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return UserCreateOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post('/favorite', response_model=UserCreateOutput, responses={418: {"model": AlternativeOutput}})
async def user_favorite_add(favorite_add: UserFavoriteInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_add.user_id, codigo=favorite_add.codigo)
        return UserCreateOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/favorite{id}')
async def user_delete(id: int):
    try:
        response = await FavoriteService.delete_favorite(id=id)
        return response
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get('/list', response_model=List[UserList])
async def user_list():
    try:
        return await UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.get('/list/{user_id}')
async def user_list(user_id: int):
    try:
        return await UserService.list_user(user_id=user_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.get('/favorite', response_model=List[FavoriteList])
async def favorite_list():
    try:
        return await FavoriteService.list_favorite()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@assets_router.get('/assets/{symbol}')
async def list_asset(symbol: str):
    try:
        return await AssetService.list_assets(symbol=symbol)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@assets_router.get('/assets_user/{user_id}')
async def list_asset_user(user_id: int):
    try:
        user = await UserService.list_user(user_id)
        favorites_symbols = [favorite.codigo_ativo for favorite in user.favorites]
        task = [AssetService.list_assets(symbol=symbol) for symbol in favorites_symbols]
        return await gather(*task)
    except Exception as error:
        raise HTTPException(400, detail=str(error))