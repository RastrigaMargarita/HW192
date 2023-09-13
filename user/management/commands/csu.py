
from django.core.management import BaseCommand
from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='rastrm@mail.ru',
            first_name='postgree',
            last_name='postgree',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('123')
        user.save()
