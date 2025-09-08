from django.shortcuts import render, get_object_or_404
from .models import Band, Concert


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
    """Render a page for booking tickets for a specific concert."""
    concert = get_object_or_404(Concert, pk=pk)
    context = {
        'concert': concert,
    }
    return render(request, 'bands/book_tickets.html', context)
