from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField("Названия",max_length=300)

    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "город"
        verbose_name_plural = "Города"


class Client(models.Model):
    first_name = models.CharField("Имя",max_length=100, blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=100, blank=True, null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE, verbose_name="Место проживание")
    profit = models.FloatField("Общая сумма выкупа",default=0,)
    telephone = models.PositiveBigIntegerField("номер телефона", blank=True, null=True, unique=True)
    telephone2 =  models.PositiveBigIntegerField("номер телефона 2", blank=True, null=True, unique=True)
    
    def __str__(self):
        return f"{self.telephone} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "Клиенты"