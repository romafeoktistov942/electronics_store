from django.core.management.base import BaseCommand
from users.models import User
from decouple import config


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **options):
        email = config("SUPERUSER_EMAIL")
        password = config("SUPERUSER_PASSWORD")

        if not User.objects.filter(email=email).exists():
            user = User.objects.create(
                email=email,
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS("Суперпользователь успешно создан")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Суперпользователь с таким email уже существует"
                )
            )
