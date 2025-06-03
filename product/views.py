import math
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F, Sum, ExpressionWrapper, Q, PositiveBigIntegerField
from datetime import datetime, timedelta

from .models import Product, Category, ProductPhoto, Transaction
from review.models import Review
from .utils.balance import get_balance


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

    return render(request, 'product.html', {"product": product, "images": images[1:], 'cover': images[0] if images else None, "products": products})


def services(request):
    return render(request, "services.html")

def statistics(request):
    month = request.GET.get('month')
    action = request.GET.get('action', 'Уход')
    # Общий фильтр по action и дате (если есть month)
    transaction_filter = Q(action=action)
    category_filter = Q(products__transaction__action=action)

    if month:
        start_date = datetime.strptime(month, "%m.%Y")
        end_date = (start_date + timedelta(days=32)).replace(day=1)
        transaction_filter &= Q(created_at__gte=start_date, created_at__lt=end_date)
        category_filter &= Q(products__transaction__created_at__gte=start_date, products__transaction__created_at__lt=end_date)

    # Общая сумма продаж за период
    total = Transaction.objects.filter(transaction_filter).aggregate(
        total=Sum(
            ExpressionWrapper(F('count') * F('price'), output_field=PositiveBigIntegerField())
        )
    )['total'] or 0

    # Продажи по категориям за период
    total_by_category = Category.objects.annotate(
        total_sales=Sum(
            ExpressionWrapper(
                F('products__transaction__count') * F('products__transaction__price'),
                output_field=PositiveBigIntegerField()
            ),
            filter=category_filter
        )
    ).order_by('-total_sales')

    total_by_category_top = total_by_category[:10]
    total_by_category_rest = sum(category.total_sales for category in total_by_category[10:] if category.total_sales)

    monthes = [date.strftime('%m.%Y') for date in Transaction.objects.dates('created_at', 'month', order='DESC')]

    # balance = get_balance()
    # print(balance)


    return render(
        request, 
        "statistics.html", 
        locals(),
    )
   
    
    
    