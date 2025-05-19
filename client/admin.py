from django.contrib import admin
from .models import Client,City
from django.utils.html import format_html
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    
    list_display = ('names','city','profit','whatsapp')
    readonly_fields = ('id', 'profit',"whatsapp",)
    search_fields = ('first_name','last_name',)
    fields = ('first_name','last_name','city','profit','telephone',"whatsapp",)

    def names(self,obj):
        return f'{obj.first_name} {obj.last_name}'

    def whatsapp(self, obj):
        
        url = f"https://wa.me/+996{obj.telephone}"
        return format_html('<a href="{}" target="_blank">{}</a>', url,url)
    whatsapp.short_description = "WhatsApp"

    class Meta:
        model = Client

admin.site.register(City)
admin.site.register(Client,ClientAdmin)

