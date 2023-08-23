"""
This module contains the functions for the random image API.
"""
from models.random_image_model import RandomImage
from services.image_service import is_valid_image_url
from sqlalchemy.exc import SQLAlchemyError


def get_random_url(session):
    """
    Get a random image URL from the database.

    Returns:
        str: A random image URL.
    """
    try:
        from sqlalchemy.sql import func

        random_url = session.query(
            RandomImage.url).order_by(func.random()).first()
        return random_url
    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific exceptions
        print(f"Error getting random image URL: {e}")
        session.rollback()
        return None
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        session.rollback()
        return None
    finally:
        session.close()


def add_url(url: str, session):
    """
    Add a new image URL to the database.
    """
    try:
        if not is_valid_image_url(url):
            raise ValueError("Invalid image URL")
        new_url = RandomImage(url=url)  # Create a new RandomImage object
        session.add(new_url)  # Add the new object to the session
        session.commit()
    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific exceptions
        print(f"Error adding image URL: {e}")
        session.rollback()
    except ValueError as e:
        # Handle invalid URL exception
        print(f"Invalid image URL: {e}")
        session.rollback()
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        session.rollback()
    finally:
        session.close()
