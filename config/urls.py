from django.contrib import admin
from django.urls import path
from product.views import home, product, products, statistics
from review.views import reviews
from service.views import services
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Администрация TechnoKB'
admin.site.index_title = 'Наши модели'
admin.site.site_title = 'Продукты - Административная панель'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('products', products),    
    path('products/<int:id>/',product),  
    path("reviews",reviews),
    path('services',services),
    path("statistics", statistics)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)