from django.shortcuts import render
from .forms import ProductForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_product import create_product, get_products
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products = get_products()
    context = {
        'product_list': products
    }
    return render(request, 'Product/products.html', context)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            create_product(form)
            messages.add_message(request, messages.SUCCESS, 'Product created successfully')
            return HttpResponseRedirect(reverse('productCreate'))
        else:
            print(form.errors)
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'Product/productCreate.html', context)
