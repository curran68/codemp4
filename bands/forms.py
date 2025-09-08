# bands/forms.py

from django import forms

class TicketBookingForm(forms.Form):
    """
    A simple form for users to book tickets.
    """
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    quantity = forms.IntegerField(label='Number of Tickets', min_value=1)