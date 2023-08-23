"""
Test cases fo the afk_count APi
"""
import pytest
from api.afk_count import get_afk_count, add_to_afk_count
from database.database import get_in_memory_db
from models.afk_count_model import AfkCount

valid_id = "1" * 18
invalid_id = "1" * 17 + "a"
id_1 = "1" * 18
id_2 = "2" * 18
id_3 = "3" * 18
invalid_id_1 = "1" * 17 + "a"
invalid_id_2 = "2" * 17 + "a"

valid_sv_id = "1" * 18
invalid_sv_id = "1" * 17 + "a"
spaces_sv_id = " " * 18
empty_sv_id = ""


@pytest.fixture
def session():
    """
    Create tables in the in-memory database and create a session.
    """
    session = get_in_memory_db()
    yield session
    session.close()


def test_add_to_afk_count(session):
    """
    Test that a user can be added to the AFK count.

    Expected Output:
        The user should be added to the AFK count.
    """
    add_to_afk_count(session, valid_id, valid_sv_id)

    afk_count = session.query(AfkCount).filter(
        AfkCount.discord_id == valid_id, AfkCount.discord_server_id == valid_sv_id).first()
    assert afk_count is not None
    assert afk_count.count == 1


def test_add_to_afk_count_invalid_id(session):
    """
    Test that a user cannot be added to the AFK count with an invalid ID.

    Expected Output:
        The user should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, invalid_id, valid_sv_id)


def test_add_to_existing_afk_count(session):
    """
    Test that a user can be added to an existing AFK count.

    Expected Output:
        The user should be added to the AFK count.
    """
    add_to_afk_count(session, valid_id, valid_sv_id)
    add_to_afk_count(session, valid_id, valid_sv_id)

    afk_count = session.query(AfkCount).filter(
        AfkCount.discord_id == valid_id, AfkCount.discord_server_id == valid_sv_id).first()
    assert afk_count is not None
    assert afk_count.count == 2


def test_multiple_users_add_to_afk_count(session):
    """
    Test that multiple users can be added to the AFK count.

    Expected Output:
        The users should be added to the AFK count.
    """
    add_to_afk_count(session, id_1, valid_sv_id)
    add_to_afk_count(session, id_2, valid_sv_id)
    add_to_afk_count(session, id_3, valid_sv_id)

    afk_count_1 = session.query(AfkCount).filter(
        AfkCount.discord_id == id_1, AfkCount.discord_server_id == valid_sv_id).first()
    afk_count_2 = session.query(AfkCount).filter(
        AfkCount.discord_id == id_2, AfkCount.discord_server_id == valid_sv_id).first()
    afk_count_3 = session.query(AfkCount).filter(
        AfkCount.discord_id == id_3, AfkCount.discord_server_id == valid_sv_id).first()

    assert afk_count_1 is not None
    assert afk_count_2 is not None
    assert afk_count_3 is not None

    assert afk_count_1.count == 1
    assert afk_count_2.count == 1
    assert afk_count_3.count == 1


def test_multiple_invalid_uses_add_to_afk_count(session):
    """
    Test that multiple users cannot be added to the AFK count with invalid IDs.

    Expected Output:
        The users should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, invalid_id_1, valid_sv_id)
    with pytest.raises(ValueError):
        add_to_afk_count(session, invalid_id_2, valid_sv_id)

    afk_count_1 = session.query(AfkCount).filter(
        AfkCount.discord_id == invalid_id_1, AfkCount.discord_server_id == valid_sv_id).first()
    afk_count_2 = session.query(AfkCount).filter(
        AfkCount.discord_id == invalid_id_2, AfkCount.discord_server_id == valid_sv_id).first()

    assert afk_count_1 is None
    assert afk_count_2 is None


def test_invalid_server_id_add_to_afk_count(session):
    """
    Test that a user cannot be added to the AFK count with an invalid server ID.

    Expected Output:
        The user should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, valid_id, invalid_sv_id)


def test_spaces_server_id_add_to_afk_count(session):
    """
    Test that a user cannot be added to the AFK count with a server ID containing spaces.

    Expected Output:
        The user should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, valid_id, spaces_sv_id)


def test_empty_server_id_add_to_afk_count(session):
    """
    Test that a user cannot be added to the AFK count with an empty server ID.

    Expected Output:
        The user should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, valid_id, empty_sv_id)


def test_all_invalid_id_add_to_afk_count(session):
    """
    Test that a user cannot be added to the AFK count with an invalid ID and server ID.

    Expected Output:
        The user should not be added to the AFK count.
    """
    with pytest.raises(ValueError):
        add_to_afk_count(session, invalid_id, invalid_sv_id)


def test_get_afk_count(session):
    """
    Test that the AFK count for a user can be retrieved.

    Expected Output:
        The AFK count for the user should be retrieved.
    """
    add_to_afk_count(session, valid_id, valid_sv_id)

    afk_count = get_afk_count(session, valid_id, valid_sv_id)
    assert afk_count == 1


def test_empty_get_afk_count(session):
    """
    """
    afk_count = get_afk_count(session, valid_id, valid_sv_id)
    assert afk_count == 0
