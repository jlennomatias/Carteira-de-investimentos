from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

#Criando a declarative_base é responsavel por integrar o orm e a sessão de banco de dados.
Base = declarative_base()


#Criando o modelo de user
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    favorites = relationship('Favorite', backref='user', lazy='subquery')

#Criando o modelo de ativos favoritos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_ativo = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))