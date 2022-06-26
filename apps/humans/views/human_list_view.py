from django.views.generic import ListView

from apps.humans.models import Human


class HumanListView(ListView):
    model = Human
