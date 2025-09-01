from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a merchant user'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address for the merchant')
        parser.add_argument('--full_name', type=str, help='Full name of the merchant', default='')
        parser.add_argument('--password', type=str, help='Password for the merchant', default='merchant123')

    def handle(self, *args, **options):
        email = options['email']
        full_name = options['full_name']
        password = options['password']

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.ERROR(f'User with email {email} already exists')
            )
            return

        merchant = User.objects.create_merchant(
            email=email,
            full_name=full_name,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created merchant: {merchant.email}')
        )
        self.stdout.write(f'Email: {merchant.email}')
        self.stdout.write(f'Password: {password}')
        self.stdout.write(f'Full Name: {merchant.full_name or "Not provided"}')
        self.stdout.write('The merchant can now log in and manage products.')