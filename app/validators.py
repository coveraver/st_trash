import re
from typing import Optional


def check_username(user_input: str) -> Optional[str]:
    """Check user input not start with number, contains only letters or digits and greater or equal to 7
    Args:
         user_input: the user input from console
    Returns:
        user input as a login or None
    """
    if len(user_input) >= 7 and user_input.isalnum() and not user_input[0].isdigit():
        return user_input
    return None


def check_password(user_input: str) -> Optional[str]:
    """Check user input contains only digits and letters and greater or equal to 7
    Args:
        user_input: the user input from console
    Returns:
        user input as password or None
    """
    if len(user_input) >= 7 and re.findall('[a-zA-Z]', user_input) and re.findall(r'\w\d+', user_input):
        return user_input
    return None


def check_username_and_password_not_equals(username: str, password: str) -> bool:
    """Check than user input for username and password not equal
    Args:
        username: user input for login from console
        password: user input for password from console
    Returns:
        True if username and password did not match and False if other case
    """
    return username != password
