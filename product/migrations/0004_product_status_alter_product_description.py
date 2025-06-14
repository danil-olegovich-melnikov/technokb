# Generated by Django 5.1 on 2025-05-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Не указано', 'Не указано'), ('Новый', 'Новый'), ('БУ', 'БУ')], default='Не указано', max_length=15, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
