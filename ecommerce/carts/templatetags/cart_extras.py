from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument."""
    try:
        return Decimal(str(value)) * Decimal(str(arg))
    except (ValueError, TypeError):
        return 0

@register.filter
def subtract(value, arg):
    """Subtracts the argument from the value."""
    try:
        return Decimal(str(value)) - Decimal(str(arg))
    except (ValueError, TypeError):
        return 0

@register.filter
def calculate_tax(subtotal, rate=0.08):
    """Calculates tax amount from subtotal."""
    try:
        return Decimal(str(subtotal)) * Decimal(str(rate))
    except (ValueError, TypeError):
        return 0