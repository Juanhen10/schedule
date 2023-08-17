from django import forms
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()


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