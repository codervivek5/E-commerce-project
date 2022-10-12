from django.shortcuts import render,HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)

    # This is a logic for fetch the product in right way
    nSlides = n//4 + ceil((n/4)-(n//4))

    print(products)
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")
    # return HttpResponse('this is about page.')

def contact(request):
    return HttpResponse('this is contact page.')

def tracker(request):
    return HttpResponse('this is tracker page.')

def search(request):
    return HttpResponse('this is search page.')

def productview(request):
    return HttpResponse('this is productview page.')

def checkout(request):
    return HttpResponse('this is checkout page.')

