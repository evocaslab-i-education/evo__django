from django.urls import path

from . import views

app_name = "session_experiments"

urlpatterns = [
    path("", views.SessionExampleView.as_view(), name="index"),
]
