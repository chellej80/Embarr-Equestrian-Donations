from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from animals.models import Animal


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        animal = get_object_or_404(Animal, pk=item_id)
        total += quantity * animal.donation
        product_count += quantity
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "animal": animal,
            }
        )

    grand_total = total

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "grand_total": grand_total,
    }

    return context
