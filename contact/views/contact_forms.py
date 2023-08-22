from django import forms
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.forms import ContactFrom
from contact.models import Contact


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactFrom(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactFrom()
    }
    return render(
        request,
        'contact/create.html',
        context
    )