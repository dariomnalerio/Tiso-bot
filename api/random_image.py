"""
This module contains the functions for the random image API.
"""
from database.database import create_session_factory
from models.random_image_model import RandomImage
from services.image_service import is_valid_image_url


def GetRandomUrl():
    """
    Get a random image URL from the database.

    This function fetches a random image URL from the database using SQLAlchemy.

    Returns:
        str: A random image URL.
    """
    from sqlalchemy.sql import func

    session = create_session_factory()
    random_url = session.query(RandomImage.url).order_by(func.random()).first()
    session.close()
    return random_url


def AddUrl(url: str, database_url: str = None):
    """
    Add a new image URL to the database.

    This function adds a new image URL to the database using SQLAlchemy.
    """
    if not is_valid_image_url(url):
        raise ValueError("Invalid image URL")
    session = create_session_factory(database_url)
    new_url = RandomImage(url=url)  # Create a new RandomImage object
    session.add(new_url)  # Add the new object to the session
    session.commit()
    session.close()
