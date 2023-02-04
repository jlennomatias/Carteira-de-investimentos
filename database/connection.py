from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite+aiosqlite:///projeto_carteira.db'

#Criando uma instancia de banco de dados chamada "engine"
engine = create_async_engine(DATABASE_URL)

#Definindo o objeto de sessão e informando que será assincrono
async_session = sessionmaker(engine, class_=AsyncSession)