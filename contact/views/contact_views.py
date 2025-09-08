from django.http import Http404
from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True)[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id).first()

    if single_contact is None:
        raise Http404()

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )