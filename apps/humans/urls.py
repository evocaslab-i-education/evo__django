from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

app_name = "humans"

urlpatterns = [
    path("", views.HumanListView.as_view(), name="show_all"),
    path("create", views.create, name="create"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit", login_required(views.HumanUpdateView.as_view()), name="edit"),
                path("delete", login_required(views.HumanDeleteView.as_view()), name="delete"),
            ]
        ),
    ),
]
