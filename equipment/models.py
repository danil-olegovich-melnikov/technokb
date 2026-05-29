from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Названия",max_length=100)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"


class Equipment(models.Model):
    name = models.CharField("Названия",max_length=100)
    description = models.CharField("Описание",max_length=300, null=True, blank=True)
    buy_price = models.PositiveIntegerField("Цена покупки", default=0)
    sell_price = models.PositiveIntegerField("Примерная цена продажи", default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория")
    created_at = models.DateTimeField("Дата",auto_now_add=True)
    

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "оборудование"
        verbose_name_plural = "Оборудование"
        ordering = ['sell_price']