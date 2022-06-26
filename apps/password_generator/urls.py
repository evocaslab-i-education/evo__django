from django.urls import path

from . import views

app_name = 'password_generator'

urlpatterns = [
    path("", views.PasswordGeneratorView.as_view(), name='index'),
    path("<int:password_length>", views.PasswordGeneratorView.as_view()),
]
