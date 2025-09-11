from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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


def book_tickets_for_concert(request, pk):
    """Renders the ticket booking page for a specific concert."""
    concert = get_object_or_404(Concert, pk=pk)
    form = TicketBookingForm()

    context = {
        'concert': concert,
        'form': form,
    }
    return render(request, 'bands/book_tickets.html', context)


def book_tickets(request):
    """General book tickets page (no specific concert)."""
    return render(request, 'bands/book_tickets.html')


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
            login(request, user)  # auto-login after registration
            return redirect('band_list')  # go to homepage
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def privacy_policy(request):
    """Privacy Policy page."""
    return render(request, 'bands/privacy_policy.html')


def terms_of_service(request):
    """Terms of Service page."""
    return render(request, 'bands/terms_of_service.html')


def contact(request):
    """Contact Us page."""
    return render(request, 'bands/contact.html')
