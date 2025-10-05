# bands/forms.py

from django import forms
from .models import ContactMessage

class TicketBookingForm(forms.Form):
    """
    A simple form for users to book tickets.
    """
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    quantity = forms.IntegerField(label='Number of Tickets', min_value=1)


class ContactForm(forms.ModelForm):
    """
    Form for contact page submissions
    """
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell us what\'s on your mind...'
            }),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Message',
        }