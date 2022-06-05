import string
from typing import Final

PASSWORD_CHARACTERS: Final[str] = ''.join([
    string.ascii_letters,
    string.digits,
])
