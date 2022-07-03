import random

from apps.password_generator.constants import PASSWORD_CHARACTERS


def generate_password(password_length: int = 10) -> str:
    password_as_list = [random.choice(PASSWORD_CHARACTERS) for _ in range(password_length)]  # noqa: B311
    random.shuffle(password_as_list)
    return "".join(password_as_list)
