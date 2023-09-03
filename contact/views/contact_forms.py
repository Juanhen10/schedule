from django import forms
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactFrom
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        context = {
            'form': form,
            'from_action': form_action,

        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id= contact.id)
    
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
            'form': ContactFrom(),
            'from_action': form_action,

        }

    return render(
        request,
        'contact/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True )
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactFrom(request.POST, isinstance = contact)
        context = {
            'form': form,
            'from_action': form_action,

        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id= contact.id)
    
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
            'form': ContactFrom(instance=contact),
            'from_action': form_action,

        }

    return render(
        request,
        'contact/create.html',
        context
    )
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )