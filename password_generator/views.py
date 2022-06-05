from django.http import HttpResponse

from password_generator.services import generate_password


def password_generator(request, password_length: int = 10):
    password = generate_password(password_length=password_length)
    return HttpResponse(f"""<p>Length of password: {len(password)}</p>
<p>{password}</p>""")
