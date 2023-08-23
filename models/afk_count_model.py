from sqlalchemy import String, Column, Integer
from models.base import Base


class AfkCount(Base):
    """
    Define a model for storing afk count data

    Attributes:
        id (int): The ID of the afk count.
        discord_id (str): The discord ID of the afk count.
        count (int): The count of afk.
    """
    __tablename__ = 'afk_count'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String, nullable=False)
    discord_server_id = Column(String, nullable=False)
    count = Column(Integer, nullable=False, default=0)
