from django.views.generic.edit import UpdateView

from apps.humans.models import Human


class HumanUpdateView(UpdateView):
    model = Human
    fields = ['name', 'age']

    # success_url = reverse_lazy('humans:show_all')
