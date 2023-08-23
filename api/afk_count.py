"""
This module contains the functions for the AFK count API
"""
from models.afk_count_model import AfkCount
from services.afk_count_service import validate_discord_id_type, validate_discord_id_length, validate_server_id_type
from sqlalchemy.exc import SQLAlchemyError


def get_afk_count(session, discord_id: str, server_id: str):
    """
    Get the current AFK count for a user.

    Args:
        session (Session): The database session.
        discord_id (str): The discord ID of the user.

    Returns:
        int: The AFK count for the user.
    """
    if not validate_discord_id_type(discord_id):
        raise ValueError("Invalid discord ID type")
    if not validate_discord_id_length(discord_id):
        raise ValueError("Invalid discord ID length")
    if not validate_server_id_type(server_id):
        raise ValueError("Invalid server ID type")

    try:
        afk_count = session.query(AfkCount.count).filter(
            AfkCount.discord_id == discord_id).first()
        if afk_count is None:
            return 0
        return afk_count[0]
    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific exceptions
        print(f"Error getting AFK count: {e}")
        session.rollback()
        return None
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        session.rollback()
        return None
    finally:
        session.close()


def add_to_afk_count(session, discord_id: str, server_id: str):
    """
    Add a user to the AFK count.

    Args:
        session (Session): The database session.
        discord_id (str): The discord ID of the user.

    Returns:
        int: The AFK count for the user. None if the user could not be added.
    """
    if not validate_discord_id_type(discord_id):
        raise ValueError("Invalid discord ID type")
    if not validate_discord_id_length(discord_id):
        raise ValueError("Invalid discord ID length")
    if not validate_server_id_type(server_id):
        raise ValueError("Invalid server ID type")

    try:
        afk_count = session.query(AfkCount).filter(
            AfkCount.discord_id == discord_id, AfkCount.discord_server_id == server_id).first()
        if afk_count is None:
            afk_count = AfkCount(discord_id=discord_id,
                                 count=1, discord_server_id=server_id)
            session.add(afk_count)
        else:
            afk_count.count += 1
        session.commit()
        return afk_count.count
    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific exceptions
        print(f"Error getting AFK count: {e}")
        session.rollback()
        return None
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        session.rollback()
        return None
    finally:
        session.close()
