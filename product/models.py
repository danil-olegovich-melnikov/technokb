from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from order.models import Order
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    name = models.CharField("Названия",max_length=100)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ["name"]

class Product(models.Model):
    name = models.CharField("Названия",max_length=100)
    category = TreeForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория", related_name="products")
    description = models.CharField("Описание",max_length=300,blank=True, null=True)    
    count = models.PositiveSmallIntegerField("Количество на текущий момент",default=0)
    total_count = models.PositiveBigIntegerField("Общая количество", default=0)
    average_price = models.FloatField("Средняя цена", default=0)
    in_stock = models.CharField("В наличии", default="Нет", max_length=3, choices=(("Да","Да"),("Нет","Нет")))
    created_at = models.DateTimeField("Дата",auto_now_add=True)
    amount_of_transaction = models.PositiveSmallIntegerField("Количество транзакций", default=0)
    is_published = models.CharField("Опубликовано", default="Нет", max_length=3, choices=(("Да","Да"),("Нет","Нет")))
   
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

class ProductPhoto(models.Model):
    image = models.ImageField("Фотография",upload_to="product", blank=True, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="Продукт")
    
    def __str__(self):
        return f"Фотография:{self.id} "

class Transaction(models.Model):
    COMING = "Приход"
    LEAVING = "Уход"
    ACTION = [
        (COMING,'Приход'),
        (LEAVING,'Уход'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    action = models.CharField("Действие",max_length=10, choices=ACTION)
    count = models.PositiveSmallIntegerField("Количество",default=0)
    price = models.FloatField("Цена")
    created_at = models.DateTimeField("Дата",auto_now_add=True)
    order = models.ForeignKey(Order,verbose_name="Заказ", on_delete=models.CASCADE, blank=True, null=True)

    
    
    
    def __str__(self):
        return f"{self.action} {self.product.name}, количество: {self.count}, цена: {self.price}"

    class Meta:
        verbose_name = "транзакция"
        verbose_name_plural = "Транзакции"


def update_product_count(instance):
    product = instance.product
    #Пересчёт общего количества:  
    transactions = Transaction.objects.filter(product = product)
    
    product.average_price = 0
    product.count = 0 
    product.total_count = 0 
    product.amount_of_transaction = 0  
    for transaction in transactions:       
        
        if transaction.action == transaction.COMING:
            product.average_price += transaction.price * transaction.count 
            product.total_count += transaction.count
            product.count += transaction.count
            
        if transaction.action == transaction.LEAVING:
            product.count -= transaction.count
            product.amount_of_transaction += 1     

    product.average_price /= product.total_count 
    product.average_price = round(product.average_price) 
    if product.count > 0:
        product.in_stock = "Да"
    else:
        product.in_stock = "Нет"
        
    product.save() 
    
    


@receiver(post_save, sender=Transaction)
def update_product_total_count(sender, instance, **kwargs):    
    update_product_count(instance)
    
@receiver(post_delete, sender=Transaction)
def update_product_total_count_on_delete(sender, instance, **kwargs):
    update_product_count(instance)

