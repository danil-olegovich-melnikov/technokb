from django.db import models
from client.models import Client

# Create your models here.

class Order(models.Model):    
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, verbose_name="Клиент", blank=True, null=True)
    image = models.ImageField("Фотография",upload_to="product", blank=True, null=True)


    
    

    def __str__(self):
        return f"{self.client}"
    
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"
