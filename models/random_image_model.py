from sqlalchemy import String, Column, Integer
from models.base import Base


class RandomImage(Base):
    __tablename__ = 'random_image'

    id = Column(Integer, primary_key=True)
    url = Column(String)
