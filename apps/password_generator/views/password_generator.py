from typing import ClassVar

from django.views.generic import TemplateView

from apps.password_generator.services import generate_password


class PasswordGeneratorView(TemplateView):
    template_name = 'password_generator/show_password.html'

    _DEFAULT_PASSWORD_LENGTH: ClassVar[int] = 10

    def get_context_data(self, **kwargs):
        # [init]-[BEGIN]
        data = super().get_context_data(**kwargs)

        try:
            password_length = data['password_length']
        except KeyError:
            password_length = self._DEFAULT_PASSWORD_LENGTH
            data['password_length'] = password_length
        # [init]-[END]

        # [action]-[BEGIN]
        password = generate_password(password_length=password_length)
        # [action]-[END]

        data['password'] = password

        return data
