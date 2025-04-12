from django.contrib import admin
from .models import Client,City
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'profit',)
    search_fields = ('first_name','last_name',)

    class Meta:
        model = Client

admin.site.register(City)
admin.site.register(Client,ClientAdmin)

