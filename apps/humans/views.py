from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import HumanForm
from .models import Human


def show_all(request: HttpRequest) -> HttpResponse:
    humans = Human.objects.all()
    return render(
        request,
        'humans/show_all.html',
        {'humans': humans},
    )


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
        'humans/edit.html',
        {'form': form},
    )


def edit(request: HttpRequest, pk) -> HttpResponse:
    human = get_object_or_404(Human, pk=pk)

    if request.POST:
        form = HumanForm(request.POST, instance=human)

        if form.is_valid():
            form.save()
            messages.info(request, 'Human edited')
            return redirect('humans:show_all')

    else:
        form = HumanForm(instance=human)

    return render(
        request,
        'humans/edit.html',
        {'form': form},
    )


def delete(request: HttpRequest, pk) -> HttpResponse:
    total_deleted, _ = Human.objects.filter(pk=pk).delete()

    if total_deleted:
        messages.warning(request, f'Humans deleted: {total_deleted}')
    else:
        messages.info(request, 'Nothing deleted')

    return redirect('humans:show_all')
