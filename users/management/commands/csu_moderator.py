from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='moderator@medcare.ru',
            first_name='admin',
            password='medcare.ru',
            is_superuser=False,
            is_staff=True,
            is_active=True,
        )
        user.set_password('medcare.ru')
        user.save()
