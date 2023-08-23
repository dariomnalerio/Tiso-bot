"""
Module for afk_count-related services.
"""


def validate_discord_id_type(discord_id: str):
    """
    Validate the type of a discord ID.

    Args:
        discord_id (str): The discord ID to validate.

    Returns:
        bool: True if the discord ID type is valid, False otherwise.
    """
    return discord_id.isdigit()


def validate_discord_id_length(discord_id: str):
    """
    Validate the length of a discord ID.

    Args:
        discord_id (str): The discord ID to validate.

    Returns:
        bool: True if the discord ID length is valid, False otherwise.
    """
    return len(discord_id) == 18


def validate_server_id_type(server_id: str):
    """
    Validate the type of a server ID.

    Args:
        server_id (str): The server ID to validate.

    Returns:
        bool: True if the server ID type is valid, False otherwise.
    """
    return server_id.isdigit()


def validate_server_id_length(server_id: str):
    """
    Validate the length of a server ID.

    Args:
        server_id (str): The server ID to validate.

    Returns:
        bool: True if the server ID length is valid, False otherwise.
    """
    return len(server_id) == 18
