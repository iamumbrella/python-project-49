import prompt


def welcome_user():
    user = prompt.string('May I have your name? ')
    return f'Hello, {user}!'
