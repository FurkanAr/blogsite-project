from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Name'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Phone'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Message'
    }))

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']