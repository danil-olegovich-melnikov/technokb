from django.shortcuts import render
from service.models import Service
# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request,"services.html", {"services": services})