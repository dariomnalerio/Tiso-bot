"""
    Module for poll-related services.
"""


def validate_question(question):
    """
        Checks whether question is empty strings.

        Args:
            question (str): The question of the poll.

        Returns:
            bool: True if the question is valid, False otherwise.
    """
    if not question.strip():
        return False

    return True


def validate_options(options):
    """
        Checks whether options are empty strings.

        Args:
            options (list): The options of the poll.

        Returns:
            bool: True if the options are valid, False otherwise.
    """
    if not options:
        return False

    return True


def validate_options_texts(options):
    """
        Checks whether option texts are empty strings.

        Args:
            options (list): The options of the poll.

        Returns:
            bool: True if the option texts are valid, False otherwise.
    """
    for option in options:
        if not option.strip():
            return False

    return True


def validate_options_type(options):
    """
        Checks whether option texts are strings.

        Args:
            options (list): The options of the poll.

        Returns:
            bool: True if the option texts are valid, False otherwise.
    """
    for option in options:
        if not isinstance(option, str):
            return False

    return True


def validate_option_text_length(options):
    """
        Checks whether option texts are too long.

        Args:
            options (list): The options of the poll.

        Returns:
            bool: True if the option texts are valid, False otherwise.
    """
    for option in options:
        if len(option) > 50:
            return False

    return True


def validate_option_list_lenght(options):
    """
        Checks whether the number of options is valid.

        Args:
            options (list): The options of the poll.

        Returns:
            bool: True if the options are valid, False otherwise.
    """
    if len(options) < 2 or len(options) > 20:
        return False

    return True
