from django.shortcuts import render,get_object_or_404
from .models import Product, Category, ProductPhoto
from django.db.models import Sum

def home(request):    
    return render(request, "homepage.html")


def products(request):
    categories = Category.objects.all().annotate(
        total_product_count=Sum('products__count')
    )
    products = Product.objects.filter(is_published = "Да", count__gt = 0) 
    return render(request, "products.html", {"categories": categories, 'products': products})


def productsold(request):
    # products = Product.objects.all()
    category_id = request.GET.get('category') 
    order = request.GET.get('order')          
    category = "Все категории"
    products = Product.objects.filter(is_published = "Да", count__gt = 0) 

    if category_id:
        category = Category.objects.get(id = category_id)
        products = products.filter(category=category_id)

    if order == "cheaper":        
        products = products.order_by('average_price') 

    elif order == "expensive":
        products = products.order_by('-average_price') 

    elif order == "new":
        products = products.order_by('-created_at')

    elif order == "popular":
        products = products.order_by('-amount_of_transaction')

    return render (request, 'products.html', { "products": products, "category": category, "order": order})
    
def product(request,id):
    product = Product.objects.get(id = id)
    images =  ProductPhoto.objects.filter(product = product)
    return render(request, 'product.html', {"product": product, "images": images})


def services(request):
    return render(request, "services.html")


   
    
    
    