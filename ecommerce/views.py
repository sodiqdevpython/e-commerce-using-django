from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory, Order
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import AddComment


def home(request):
    products = Product.objects.all()[:8]
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_detail(request, pk):
    get_data = get_object_or_404(Product, id=pk)
    if request.user.is_authenticated:
        is_ordered = Order.objects.filter(user=request.user, product=get_data)
        context = {
            'product': get_data,
            'is_ordered': is_ordered.count()
        }
    else:
        context = {
            'product': get_data
        }

    return render(request, 'product-detail.html', context)


def store(request):
    get_data = Product.objects.all()
    cats = ProductCategory.objects.all()

    context = {
        'cats': cats,
        'get_data': get_data
    }

    return render(request, 'store.html', context)


def filtering_view(request, name):
    cats = ProductCategory.objects.all()
    get_data = Product.objects.filter(category__name=name)

    context = {
        'cats': cats,
        'get_data': get_data
    }

    return render(request, 'store.html', context)


def search_product(request):
    searched_for = request.GET.get('q')
    get_data = Product.objects.filter(
        Q(name__icontains=searched_for)
    )
    print(searched_for)
    context = {
        'cats': ProductCategory.objects.all(),
        'get_data': get_data
    }
    return render(request, 'search-result.html', context)


@login_required
def card_view(request):
    get_data = Order.objects.filter(user=request.user)
    price = 0
    for i in get_data:
        price += i.product.price

    context = {
        'get_data': get_data,
        'price': price
    }
    return render(request, 'cart.html', context)


@login_required
def add_to_card(request, pk):
    product = get_object_or_404(Product, id=pk)
    new_order = Order.objects.create(
        user=request.user,
        product=product,
    )
    new_order.save()

    return redirect('product_detail', pk)


@login_required
def delete_card(request, id):
    deleting_item = get_object_or_404(Order, id=id)
    deleting_item.delete()
    return redirect('card')


@login_required
def dashboard(request):
    user_orders = Order.objects.filter(user=request.user, status='P')

    context = {
        'user_orders': user_orders
    }

    return render(request, 'dashboard.html', context)