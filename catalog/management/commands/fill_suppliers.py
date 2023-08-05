# myapp/management/commands/fill.py
from django.core.management import BaseCommand

from catalog.models import Supplier


class Command(BaseCommand):

    def handle(self, *args, **options):
        supplier_list = [
            {'name': 'Золотая семечка'},
            {'name': 'Berison'},
            {'name': 'Africa export'}
        ]

        supplier_to_create = []

        for item in supplier_list:
            supplier_to_create.append(Supplier(**item))

        Supplier.objects.bulk_create(supplier_to_create)
