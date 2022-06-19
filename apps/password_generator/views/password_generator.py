from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.password_generator.services import generate_password


def password_generator(request: HttpRequest, password_length: int = 10) -> HttpResponse:
    password = generate_password(password_length=password_length)
    return render(
        request,
        'password_generator/show_password.html',
        {'password': password, 'password_length': len(password)},
    )
