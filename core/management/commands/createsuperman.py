from users.models import CustomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email='admin@gmail.com').exists():
            CustomUser.objects.create_superuser(
                email='admin',
                first_name='Super',
                last_name='Man',
                phone_number='01222927392',
                password='complexpassword123'
            )
        print('Superuser has been created.')