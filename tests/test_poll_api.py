"""
Test cases for the poll API
"""
import pytest
from api.poll import create_poll
from database.database import get_in_memory_db
from models.poll_model import Poll

valid_question = "What is your favorite programming language?"
valid_options = ["Python", "Java", "C++", "JavaScript"]

# Mocking the database URL for testing purposes


@pytest.fixture
def session():
    """
    Create tables in the in-memory database and create a session.
    """
    session = get_in_memory_db()
    yield session
    session.close()


def test_create_poll(session):
    """
    Test that a poll can be created.

    This test checks that a poll can be created using the create_poll function.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    poll_id = create_poll(session, valid_question, valid_options)

    assert poll_id is not None

    poll = session.query(Poll).filter_by(id=poll_id).first()
    assert poll is not None
    assert poll.question == valid_question
    poll_option_texts = [option.option_text for option in poll.options]
    assert poll_option_texts == valid_options


def test_create_poll_invalid_question(session):
    """
    Test that a poll cannot be created with an invalid question.

    This test checks that a poll cannot be created using the create_poll function
    if the question is invalid.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, "", valid_options)


def test_create_poll_invalid_options(session):
    """
    Test that a poll cannot be created with invalid options.

    This test checks that a poll cannot be created using the create_poll function
    if the options are invalid.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, [])


def test_create_poll_invalid_options_type(session):
    """
    Test that a poll cannot be created with invalid option types.

    This test checks that a poll cannot be created using the create_poll function
    if the option types are invalid.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, [1, 2, 3])


def test_create_poll_invalid_options_texts(session):
    """
    Test that a poll cannot be created with invalid option texts.

    This test checks that a poll cannot be created using the create_poll function
    if the option texts are invalid.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, ["", "Python", "Java", "C++"])


def test_create_poll_invalid_option_text_length(session):
    """
    Test that a poll cannot be created with invalid option text length.

    This test checks that a poll cannot be created using the create_poll function
    if the option text length is invalid.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, [
                    "P" * 51, "Python", "Java", "C++"])


def test_create_poll_invalid_short_options_lenght(session):
    """
    Test that a poll cannot be created with invalid options length.

    This test checks that a poll cannot be created using the create_poll function
    if the options length is less than 2.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, ["Python"])


def test_create_poll_invalid_long_options_lenght(session):
    """
    Test that a poll cannot be created with invalid options length.

    This test checks that a poll cannot be created using the create_poll function
    if the options length is greater than 20.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    with pytest.raises(ValueError):
        create_poll(session, valid_question, ["Python"] * 21)