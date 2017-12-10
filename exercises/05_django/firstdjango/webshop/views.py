from django.http import HttpResponse, Http404
from django.shortcuts import render
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "webshop/product_view.html", {"product": product})

def available_products(request):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
    try:
        products = Product.objects.filter(quantity__gt=0)
    except Product.DoesNotExist:
        raise Http404("Products does not exist")
    return render(request, "webshop/product_list.html", {"products": products})
