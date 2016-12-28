from django import forms

# defines the contact form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=32)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=140)
