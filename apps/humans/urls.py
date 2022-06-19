from django.urls import path, include

from . import views

app_name = 'humans'

urlpatterns = [
    path("", views.show_all, name='show_all'),
    path("create", views.create, name='create'),
    path("<int:pk>/", include([
        path('edit', views.edit, name='edit'),
        path('delete', views.delete, name='delete'),
    ])),

]
