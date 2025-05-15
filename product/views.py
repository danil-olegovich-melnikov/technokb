import math
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Sum

from .models import Product, Category, ProductPhoto
from review.models import Review



def home(request):  
    reviews = Review.objects.all() [:3]
    
    return render(request, "homepage.html",{"reviews": reviews})


def products(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_published = "Да", count__gt = 0)
    order = request.GET.get('order')          
    category = request.GET.get('category')          
    page = int(request.GET.get('page', 1))          

    if category:
        category = Category.objects.get(id=category)
        products = products.filter(category=category)
    
    total_products = len(products)
    count = 8
    pages = math.ceil(total_products / count)
    
    if order == "cheaper":        
        products = products.order_by('average_price') 

    elif order == "expensive":
        products = products.order_by('-average_price') 

    elif order == "new":
        products = products.order_by('-created_at')

    elif order == "popular":
        products = products.order_by('-amount_of_transaction')


    products = products[(page-1) * count : count * page]

    
    return render(
        request, 
        "products.html", 
        {
            "categories": categories, 
            'products': products, 
            'order': order, 
            'category': 
            category, 'pages': 
            range(1, pages+1), 
            'page': page
        }
    )


def product(request,id):
    product = Product.objects.get(id = id)
    images =  ProductPhoto.objects.filter(product = product)
    products = Product.objects.filter(is_published = "Да", count__gt = 0)[:12]

    return render(request, 'product.html', {"product": product, "images": images, "products": products})


def services(request):
    return render(request, "services.html")


   
    
    
    