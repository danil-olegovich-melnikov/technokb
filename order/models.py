from django.db import models
from client.models import Client

# Create your models here.

class Order(models.Model):    
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, verbose_name="Клиент", blank=True, null=True)
    image = models.ImageField("Фотография",upload_to="product", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления",auto_now=True)


    def __str__(self):
        return f"{self.client}"
    
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"
