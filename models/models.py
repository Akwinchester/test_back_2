from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME
from datetime import datetime
# Создание подключения к базе данных
engine = create_engine(f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Определение базовой модели
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
