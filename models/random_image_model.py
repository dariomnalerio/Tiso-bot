from sqlalchemy import String, Column, Integer
from models.base import Base


class RandomImage(Base):
    """
    Define a model for storing random image data

    Attributes:
        id (int): The ID of the image.
        url (str): The URL of the image.
    """
    __tablename__ = 'random_image'

    id = Column(Integer, primary_key=True)
    url = Column(String)
