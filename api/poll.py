"""
    This module contains the functions for the poll API.
"""
from models.poll_model import Poll, PollOption
from database.database import create_tables
from sqlalchemy.exc import SQLAlchemyError
from services.poll_service import validate_question, validate_option_text_length, validate_options_texts, validate_options, validate_options_type, validate_option_list_lenght


def create_poll(session, question, options):
    """
    Add a new poll to the database.

    Returns:
        int: The ID of the new poll, or None on failure.
    """

    # Validate input data
    if not validate_question(question):
        raise ValueError("Question is required")

    if not validate_options(options):
        raise ValueError("Options are required")

    if not validate_option_list_lenght(options):
        raise ValueError("Options must be between 2 and 20")

    if not validate_options_type(options):
        raise ValueError("Options must be strings")

    if not validate_options_texts(options):
        raise ValueError("Option text is required for all options")

    if not validate_option_text_length(options):
        raise ValueError("Option text cannot be longer than 50 characters")

    try:
        # Create a new Poll object
        new_poll = Poll(question=question)

        # Create PollOption objects and associate them with the Poll
        for option_text in options:
            poll_option = PollOption(option_text=option_text)
            new_poll.options.append(poll_option)

        session.add(new_poll)  # Add the new object to the session
        session.commit()
        return new_poll.id
    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific exceptions (e.g., integrity errors)
        print(f"Error creating poll: {e}")
        session.rollback()  # Roll back the transaction to maintain data integrity
        return None
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        session.rollback()  # Roll back the transaction
        return None
    finally:
        session.close()
