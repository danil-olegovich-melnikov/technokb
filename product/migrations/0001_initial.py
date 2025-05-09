# Generated by Django 5.1 on 2025-04-12 06:09

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество на текущий момент')),
                ('total_count', models.PositiveBigIntegerField(default=0, verbose_name='Общая количество')),
                ('average_price', models.FloatField(default=0, verbose_name='Средняя цена')),
                ('in_stock', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='В наличии')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('amount_of_transaction', models.PositiveSmallIntegerField(default=0, verbose_name='Количество транзакций')),
                ('is_published', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Опубликовано')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Фотография')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Приход', 'Приход'), ('Уход', 'Уход')], max_length=10, verbose_name='Действие')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]
