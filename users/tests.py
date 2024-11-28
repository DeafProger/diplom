from django.test import TestCase
from users.models import User


# Create your tests here.
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Big', last_name='Bob',
                            email='my@big-bob.com')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'имя')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'фамилия')

    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_first_name_defis_email(self):
        user = User.objects.get(id=1)
        expected_object_name = '%s - %s' % (user.first_name, user.email)
        self.assertEqual(expected_object_name, str(user))
