from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='health_moderator@localhost',
            first_name='admin',
            password='12345',
            is_superuser=False,
            is_staff=True,
            is_active=True,
        )
        user.set_password('Blev2011')
        user.save()