"""
Test cases for poll_service.py
"""
from services.poll_service import validate_question, validate_options_texts, validate_options_type, validate_option_text_length, validate_options, validate_option_list_lenght


valid_question = "What is your favorite programming language?"
valid_options = ["Python", "Java", "C++", "JavaScript"]
invalid_question = ""
invalid_options = []
wrong_type_options = [b"0101"]

# Validate Input Data Tests


def test_validate_valid_question():
    """
    Test valid question validation with `validate_question` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_question(valid_question)

    assert is_valid


def test_validate_invalid_question():
    """
    Test invalid question validation with `validate_question` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_question(invalid_question)

    assert not is_valid


def test_validate_valid_options():
    """
    Test valid options validation with `validate_options` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_options(valid_options)

    assert is_valid


def test_validate_invalid_options():
    """
    Test invalid options validation with `validate_options` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_options(invalid_options)

    assert not is_valid


def test_validate_valid_options_texts():
    """
    Test valid option texts validation with `validate_options_texts` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_options_texts(valid_options)

    assert is_valid


def test_validate_valid_options_type():
    """
    Test valid option text type validation with `validate_input_data` function.

    Expected Output:
        The function should return True.
    """
    is_valid = validate_options_type(valid_options)

    assert is_valid


def test_validate_invalid_options_type():
    """
    Test invalid option text type validation with `validate_input_data` function.

    Expected Output:
        The function should return False.
    """
    is_valid = validate_options_type(wrong_type_options)

    assert not is_valid


def test_validate_valid_option_lenght():
    """
    Test valid option list lenght validation with `validate_option_list_lenght` function.

    Expected Output:
        The function should return True
    """
    is_valid = validate_option_list_lenght(valid_options)

    assert is_valid


def test_validate_invalid_short_option_lenght():
    """
    Test invalid option list lenght validation with `validate_option_list_lenght` function.

    Expected Output:
        The function should return False
    """
    is_valid = validate_option_list_lenght(["P"])

    assert not is_valid


def test_validate_invalid_long_option_lenght():
    """
    Test invalid option list lenght validation with `validate_option_list_lenght` function.

    Expected Output:
        The function should return False
    """
    is_valid = validate_option_list_lenght(["P"] * 21)

    assert not is_valid
