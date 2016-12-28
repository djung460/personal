from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from . import forms


# Create your views here.

def index(request):
    form_class = forms.ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
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
            return redirect('index')

    return render(request, 'personal/home.html', {'form': form_class})


def demos(request):
    return render(request, 'personal/demos.html')
