from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from apps.humans.forms import HumanForm


def create(request: HttpRequest) -> HttpResponse:
    if request.POST:
        form = HumanForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Human created')
            return redirect('humans:show_all')

    else:
        form = HumanForm()

    return render(
        request,
        'humans/human_form.html',
        {'form': form},
    )
