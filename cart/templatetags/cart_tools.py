from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(donation, quantity):
    return donation * quantity