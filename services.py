from aiohttp import ClientSession
from database.models import User, Favorite
from database.connection import async_session
from sqlalchemy import delete
from sqlalchemy.future import select


class UserService:
    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()

    async def list_user(user_id: int):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id==user_id))
            return result.scalars().one()
    
    async def list_users():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

class FavoriteService:
    async def add_favorite(user_id: int, codigo: str):
        async with async_session() as session:
            session.add(Favorite(user_id=user_id, codigo_ativo=codigo))
            await session.commit()

    async def delete_favorite(id: int):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(Favorite.id==id))
            await session.commit()

    async def list_favorite():
        async with async_session() as session:
            result = await session.execute(select(Favorite))
            return result.scalars().all()

class AssetService:
    async def list_assets(symbol: str):
        async with ClientSession() as session:
            url = f'https://www.mercadobitcoin.net/api/{symbol}/ticker/'
            response = await session.get(url)
            return await response.json()