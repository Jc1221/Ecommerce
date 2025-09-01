from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404

from products.models import Product
from products.forms import ProductForm


def merchant_required(view_func):
    """Decorator to ensure only merchants can access the view"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_merchant and not request.user.is_admin:
            raise PermissionDenied("You must be a merchant to access this page.")
        return view_func(request, *args, **kwargs)
    return wrapper


@merchant_required
def merchant_dashboard(request):
    """Dashboard for merchants to manage their products"""
    products = Product.objects.filter(merchant=request.user)
    active_products = products.filter(active=True)
    inactive_products = products.filter(active=False)
    featured_products = products.filter(featured=True)
    
    context = {
        'products': products,
        'active_products': active_products,
        'inactive_products': inactive_products,
        'featured_products': featured_products,
        'total_products': products.count(),
        'active_count': active_products.count(),
        'inactive_count': inactive_products.count(),
        'featured_count': featured_products.count(),
        'title': 'Merchant Dashboard'
    }
    return render(request, 'merchants/dashboard.html', context)


@merchant_required
def merchant_product_list(request):
    """List all products for the current merchant"""
    products = Product.objects.filter(merchant=request.user)
    
    # Filter by status if requested
    status_filter = request.GET.get('status')
    if status_filter == 'active':
        products = products.filter(active=True)
    elif status_filter == 'inactive':
        products = products.filter(active=False)
    
    context = {
        'products': products,
        'title': 'My Products',
        'status_filter': status_filter
    }
    return render(request, 'merchants/product_list.html', context)


@merchant_required
def merchant_product_create(request):
    """Create a new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.merchant = request.user
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect('merchants:product_list')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'title': 'Create Product'
    }
    return render(request, 'merchants/product_form.html', context)


@merchant_required
def merchant_product_edit(request, product_id):
    """Edit an existing product (only merchant's own products)"""
    product = get_object_or_404(Product, id=product_id, merchant=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('merchants:product_list')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'title': 'Edit Product'
    }
    return render(request, 'merchants/product_form.html', context)


@merchant_required
def merchant_product_delete(request, product_id):
    """Delete a product (only merchant's own products)"""
    product = get_object_or_404(Product, id=product_id, merchant=request.user)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('merchants:product_list')
    
    context = {
        'product': product,
        'title': 'Delete Product'
    }
    return render(request, 'merchants/product_confirm_delete.html', context)


@merchant_required
def merchant_product_toggle_active(request, product_id):
    """Toggle product active status"""
    product = get_object_or_404(Product, id=product_id, merchant=request.user)
    product.active = not product.active
    product.save()
    
    status = "activated" if product.active else "deactivated"
    messages.success(request, f'Product {status} successfully!')
    return redirect('merchants:product_list')