from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
import datetime
from . import forms, models


# Create your views here.

def index(request):
    form_class = forms.ContactForm

    is_contact_sent = False;

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            contact = models.Contact(name=name, email=email, message=message,date=datetime.datetime.now())

            # performs check before saving
            contact.check_save()

            is_contact_sent = True

            # Email the profile with the
            # contact information
            # store
            """
            TODO: store this in a log somewhere later
            template = get_template('contact_template.txt')

            context = Context({
                'name': name,
                'email': email,
                'message': message,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            """

            return render(request, 'personal/home.html', {'form': form_class, 'success': is_contact_sent})

    return render(request, 'personal/home.html', {'form': form_class, 'success': is_contact_sent})


def demos(request):
    return render(request, 'personal/demos.html')
