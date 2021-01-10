from app.validators import (
    check_username,
    check_password,
    check_username_and_password_not_equals
)


def register_user() -> bool:
    """Register user in system
    Returns:
        True if user registered succeed
    """
    register = False
    credentials = {}
    print('SIGN UP')

    while not register:
        username = input('Enter a USERNAME.\nUsername must be more than 6 characters: ')
        password = input('Enter a PASSWORD.\nPassword must contain numbers, letters and be more than 6 characters!'
                         'Also must not equal with username: ')
        if check_username(username):
            valid_password = False
            while not valid_password:
                password = check_password(password)
                if password and check_username_and_password_not_equals(username, password):
                    credentials[username] = password
                    print(f'Registration complete\n{credentials}')
                    register = True
                    return register
                else:
                    password = input(
                        'Enter a PASSWORD.\nPassword must contain numbers, letters and be more than 6 characters!'
                        'Also must not equal with username: ')


if __name__ == '__main__':
    register_user()
