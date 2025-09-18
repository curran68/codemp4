# cart/contexts.py

from decimal import Decimal
from django.conf import settings

def cart_contents(request):
    """
    A context processor to make the cart contents
    available to all templates.
    """
    cart_items = []
    total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context