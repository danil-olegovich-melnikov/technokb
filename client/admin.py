from django.contrib import admin
from .models import Client,City
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    search_fields = ('first_name','last_name', 'telephone')
    list_display = ('telephone', 'first_name', 'last_name', 'city')
    autocomplete_fields = ['city',]
    exclude = ('profit', )  

    class Meta:
        model = Client

admin.site.register(City, CityAdmin)
admin.site.register(Client,ClientAdmin)

