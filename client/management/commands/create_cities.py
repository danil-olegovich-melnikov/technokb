from django.core.management.base import BaseCommand
from client.models import City


class Command(BaseCommand):
    help = "Create cities if they do not exist"

    def handle(self, *args, **options):
        cities = [
            "Кара-Балта",
            "Алексеевка",
            "Беловодск",
            "Сокулук",
            "Александровка",
            "Бишкек",
            "Вознесеновка",
            "Панфиловка",
            "Чалдовар",
            "Каинда",
            "Новониколаевка",
            "Петровка",
            "Ош",
            "Кант",
        ]

        created_count = 0

        for city_name in cities:
            city, created = City.objects.get_or_create(name=city_name)

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {city.name}"))
            else:
                self.stdout.write(f"Already exists: {city.name}")

        self.stdout.write(
            self.style.SUCCESS(f"Done. Created {created_count} cities.")
        )