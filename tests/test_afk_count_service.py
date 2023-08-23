"""
Test cases for afk_count_service.py
"""
from services.afk_count_service import validate_discord_id_length, validate_discord_id_type, validate_server_id_type

valid_id = "1" * 18
invalid_id = "1" * 17 + "a"
short_id = "1"
long_id = "1" * 19
spaces_id = " " * 18
empty_id = ""

valid_sv_id = "1" * 18
invalid_sv_id = "1" * 17 + "a"
short_sv_id = "1"
long_sv_id = "1" * 19
spaces_sv_id = " " * 18
empty_sv_id = ""


def test_valid_discord_id_type():
    """
    Test valid discord ID type validation with `validate_discord_id_type` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_discord_id_type(valid_id)

    assert is_valid


def test_invalid_discord_id_type():
    """
    Test invalid discord ID type validation with `validate_discord_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_type(invalid_id)

    assert not is_valid


def test_empty_discord_id_type():
    """
    Test empty discord ID type validation with `validate_discord_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_type(empty_id)

    assert not is_valid


def test_space_discord_id_type():
    """
    Test space discord ID type validation with `validate_discord_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_type(spaces_id)

    assert not is_valid


def test_valid_discord_id_length():
    """
    Test valid discord ID length validation with `validate_discord_id_length` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_discord_id_length(valid_id)

    assert is_valid


def test_invalid_long_discord_id_length():
    """
    Test long invalid discord ID length validation with `validate_discord_id_length` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_length(long_id)

    assert not is_valid


def test_invalid_short_discord_id_length():
    """
    Test short invalid discord ID length validation with `validate_discord_id_length` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_length(short_id)

    assert not is_valid


def test_invalid_short_discord_id_length2():
    """
    Test short invalid discord ID length validation with `validate_discord_id_length` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_length("1" * 17)

    assert not is_valid


def test_invalid_empty_discord_id_length():
    """
    Test empty invalid discord ID length validation with `validate_discord_id_length` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_discord_id_length(empty_id)

    assert not is_valid


def test_valid_server_id_type():
    """
    Test valid server ID type validation with `validate_server_id_type` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_server_id_type(valid_sv_id)

    assert is_valid


def test_invalid_server_id_type():
    """
    Test invalid server ID type validation with `validate_server_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_server_id_type(invalid_sv_id)

    assert not is_valid


def test_empty_server_id_type():
    """
    Test empty server ID type validation with `validate_server_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_server_id_type(empty_sv_id)

    assert not is_valid


def test_space_server_id_type():
    """
    Test space server ID type validation with `validate_server_id_type` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_server_id_type(spaces_sv_id)

    assert not is_valid
