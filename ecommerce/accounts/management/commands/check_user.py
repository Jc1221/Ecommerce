from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Check user status and fix login issues'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address to check')
        parser.add_argument('--activate', action='store_true', help='Activate the user if inactive')
        parser.add_argument('--reset-password', type=str, help='Reset password to specified value')

    def handle(self, *args, **options):
        email = options['email']
        
        try:
            user = User.objects.get(email=email)
            self.stdout.write(f"Found user: {user.email}")
            self.stdout.write(f"Active: {user.active}")
            self.stdout.write(f"Staff: {user.staff}")
            self.stdout.write(f"Admin: {user.admin}")
            self.stdout.write(f"Merchant: {user.merchant}")
            
            if options['activate'] and not user.active:
                user.active = True
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Activated user: {user.email}')
                )
            
            if options['reset_password']:
                user.set_password(options['reset_password'])
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Reset password for user: {user.email}')
                )
                
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User with email {email} does not exist')
            )