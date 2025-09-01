from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Order
from addresses.models import Address


@login_required
def user_profile(request):
    """User profile page"""
    context = {
        'title': 'My Profile',
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def user_addresses(request):
    """User addresses management"""
    from billing.models import BillingProfile
    
    billing_profile, created = BillingProfile.objects.get_or_create(
        user=request.user,
        defaults={'email': request.user.email}
    )
    
    addresses = Address.objects.filter(billing_profile=billing_profile)
    
    context = {
        'title': 'My Addresses',
        'addresses': addresses,
        'billing_profile': billing_profile
    }
    return render(request, 'accounts/addresses.html', context)


@login_required
def user_order_history(request):
    """User order history"""
    from billing.models import BillingProfile
    
    try:
        billing_profile = BillingProfile.objects.get(user=request.user)
        orders = Order.objects.filter(billing_profile=billing_profile).order_by('-timestamp')
    except BillingProfile.DoesNotExist:
        orders = []
    
    context = {
        'title': 'Order History',
        'orders': orders
    }
    return render(request, 'accounts/order_history.html', context)