# bands/views.py

import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Band, Concert
from .forms import TicketBookingForm


def band_list(request):
    """Show a list of all bands."""
    bands = Band.objects.all()
    return render(request, 'bands/bands.html', {'bands': bands})


def concert_list(request):
    """Show a list of all concerts."""
    concerts = Concert.objects.all()
    return render(request, 'bands/concert_list.html', {'concerts': concerts})


def band_detail(request, slug):
    """Show details for a single band."""
    band = get_object_or_404(Band, slug=slug)
    return render(request, 'bands/band_detail.html', {'band': band})


def book_tickets(request, pk):
    """
    Renders the ticket booking page for a specific concert
    and handles form submission for Stripe checkout.
    """
    concert = get_object_or_404(Concert, pk=pk)
    
    # Handle the form submission (POST request) for creating a Stripe session
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        quantity = request.POST.get('quantity', 1)  # Get quantity from the form

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': f"{concert.name} Ticket",
                        },
                        'unit_amount': 2000, # £20.00
                    },
                    'quantity': quantity,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('success/'),
                cancel_url=request.build_absolute_uri('cancel/'),
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            # Handle Stripe-specific errors
            return render(request, 'bands/error_page.html', {'error': str(e)})

    # Render the booking form (GET request)
    form = TicketBookingForm()
    context = {
        'concert': concert,
        'form': form,
    }
    return render(request, 'bands/book_tickets.html', context)


def payment_success(request):
    """Render the success page after a successful payment."""
    return render(request, 'bands/payment_success.html')


def payment_cancel(request):
    """Render the cancellation page after a cancelled payment."""
    return render(request, 'bands/payment_cancel.html')


@login_required
def profile_view(request):
    """User profile page - requires login."""
    context = {
        'user': request.user,
    }
    return render(request, 'bands/profile.html', context)


def register_view(request):
    """User registration page with Django's built-in form."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('band_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})