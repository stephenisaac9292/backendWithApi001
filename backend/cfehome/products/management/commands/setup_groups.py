# your_app/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

class Command(BaseCommand):
    help = 'Set up user groups and assign default permissions'

    def handle(self, *args, **options):
        Product = apps.get_model('products', 'Products')  # replace with your actual model
        productPermissionFetch = ContentType.objects.get_for_model(Product)

        # Customer: view only
        customer_group, _ = Group.objects.get_or_create(name='Customer')
        customer_perms = Permission.objects.filter(
            content_type= productPermissionFetch,
            codename__in=['view_product']
        )
        customer_group.permissions.set(customer_perms)

        # Seller: add, change, view
        seller_group, _ = Group.objects.get_or_create(name='Seller')
        seller_perms = Permission.objects.filter(
            content_type= productPermissionFetch,
            codename__in=['add_product', 'change_product', 'view_product']
        )
        seller_group.permissions.set(seller_perms)

        # Staff: manage users and view products
        staff_group, _ = Group.objects.get_or_create(name='Staff')
        userPermissionFetch = ContentType.objects.get(app_label='auth', model='user')
        staff_perms = Permission.objects.filter(
            content_type__in=[productPermissionFetch, userPermissionFetch],
            codename__in=['view_user', 'add_user', 'change_user', 'view_product']
        )
        staff_group.permissions.set(staff_perms)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created!"))
