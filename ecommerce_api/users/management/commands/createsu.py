from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Creates a superuser if it doesn't exist"
    
    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ.get('SUPERUSER_EMAIL', 'deenyashke@gmail.com')
        password = os.environ.get('SUPERUSER_PASSWORD', 'password')
        
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superuser {email} created successfully')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Superuser {email} already exists')
            )