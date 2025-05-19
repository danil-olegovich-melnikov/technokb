from django.shortcuts import render
from service.models import Category, Service
# Create your views here.

def services(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    selected_category = request.GET.get("category")
    
    if selected_category:
        services = services.filter(category__id=selected_category)
        selected_category = int(selected_category)
    
    return render(
        request,
        "services.html", 
        {
            "services": services, 
            "categories": categories, 
            "selected_category": selected_category
        }
    )