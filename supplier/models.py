from django.db import models
from client.models import City

# Create your models here.
class Suplier(models.Model):
    first_name = models.CharField("Имя",max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE, verbose_name="Место проживание")
    profit = models.FloatField("Общая сумма выкупа",default=0,)
    telephone = models.PositiveBigIntegerField("номер телефона", blank=True, null=True)
    telephone2 =  models.PositiveBigIntegerField("номер телефона 2", blank=True, null=True)
    categories = models.ManyToManyField('product.category', verbose_name='Категории')
    def __str__(self):
        return f"{self.telephone} - {self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "поставщика"
        verbose_name_plural = "Поставщики"


class SuplierOrder(models.Model):    
    suplier = models.ForeignKey(Suplier,on_delete=models.SET_NULL, verbose_name="Поставщик", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления",auto_now=True)


    def __str__(self):
        return f"{self.suplier}"
    
    class Meta:
        verbose_name = "поставка"
        verbose_name_plural = "Поставки"