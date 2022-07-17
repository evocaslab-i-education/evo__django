import pytest

from apps.password_generator.services import generate_password


@pytest.mark.parametrize(
    "input_length,output_length",
    [
        (10, 10),
        (20, 20),
    ],
)
def test_password_generator(input_length: int, output_length: int):
    password = generate_password(input_length)
    assert len(password) == output_length  # noqa: B101
