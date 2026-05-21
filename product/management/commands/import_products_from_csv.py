import csv
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from product.models import Category, Product, Transaction


class Command(BaseCommand):
    help = "Import categories, products and income transactions from CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            required=True,
            help="Path to CSV file",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        file_path = options["file"]

        created_categories = 0
        created_products = 0
        created_transactions = 0

        with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                category_name = row["Категория"].strip()
                product_name = row["Наименования"].strip()
                quantity = int(row["Количество"])
                purchase_price = Decimal(row["Цена закупа"])

                category, category_created = Category.objects.get_or_create(
                    name=category_name
                )
                if category_created:
                    created_categories += 1

                product, product_created = Product.objects.get_or_create(
                    name=product_name,
                    defaults={
                        "category": category,
                    },
                )

                if product_created:
                    created_products += 1
                else:
                    if product.category_id != category.id:
                        product.category = category
                        product.save(update_fields=["category"])

                Transaction.objects.create(
                    product=product,
                    action=Transaction.COMING,
                    count=quantity,
                    price=purchase_price,
                )
                created_transactions += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. Categories: {created_categories}, "
                f"Products: {created_products}, "
                f"Transactions: {created_transactions}"
            )
        )