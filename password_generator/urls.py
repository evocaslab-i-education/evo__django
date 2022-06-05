from django.urls import path

from . import views

urlpatterns = [
    path('', views.password_generator),
    path('<int:password_length>', views.password_generator)
]
