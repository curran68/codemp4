from django.shortcuts import render, get_object_or_404
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
    """
    Renders the ticket booking page for a specific concert.
    """
    concert = get_object_or_404(Concert, pk=pk)
    form = TicketBookingForm()

    context = {
        'concert': concert,
        'form': form,
    }
    return render(request, 'bands/book_tickets.html', context)


def book_tickets(request):
    """
    General book tickets page (no specific concert).
    """
    return render(request, 'bands/book_tickets.html')


def login_view(request):
    return render(request, 'bands/login.html')


def register_view(request):
    return render(request, 'bands/register.html')


def profile_view(request):
    return render(request, 'bands/profile.html')