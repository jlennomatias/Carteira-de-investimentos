
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+asyncpg://admin:psltest@192.168.59.100:30356/postgresdb'

#Criando uma instancia de banco de dados chamada "engine"
engine = create_async_engine(DATABASE_URL)
#Definindo o objeto de sessão e informando que será assincrono
async_session = sessionmaker(engine, class_=AsyncSession)