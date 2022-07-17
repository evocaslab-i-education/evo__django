from django.urls import path

from . import views

app_name = "sessions_example"

urlpatterns = [
    path("", views.SessionExample.as_view(), name="index"),
]
