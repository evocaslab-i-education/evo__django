from django.contrib.auth.forms import UserCreationForm

from apps.users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
