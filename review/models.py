from django.db import models
from client.models import Client
from django.core.validators import MinValueValidator, MaxValueValidator


class Resurce(models.Model):
    name = models.CharField("Названия", max_length=200)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "источник"
        verbose_name_plural = "Источники"    

class Review(models.Model):
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    avatar = models.ImageField("Аватарка",upload_to="avatar", blank=True, null=True)
    date = models.DateTimeField("Дата")
    raiting = models.IntegerField("Оценка", validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField("Комментарий")
    image = models.ImageField("Фотография",upload_to="review", blank=True, null=True)

    def __str__(self):
        return f"{self.client}"
    
    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"