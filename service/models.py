from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField("Названия",max_length=200)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"    


class Service(models.Model):
    title = models.CharField("Названия",max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField("описание")
    image = models.ImageField("Фотография",upload_to="service", blank=True, null=True)
    price = models.PositiveSmallIntegerField("Цена")

    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "Сервисы" 