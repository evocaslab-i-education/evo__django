from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.humans.models import Human


class HumanDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        total_deleted, _ = Human.objects.filter(pk=pk).delete()

        if total_deleted:
            messages.warning(request, f'Humans deleted: {total_deleted}')
        else:
            messages.info(request, 'Nothing deleted')

        return redirect('humans:show_all')
