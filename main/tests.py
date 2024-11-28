from django.test import TestCase
from main.models import Doctor


# Create your tests here.
class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Doctor.objects.create(name='Big', surname='Bob',
                              specialization='Врач',
                              qualification='ДМН',
                              experience=20)

    def test_first_name_label(self):
        user = Doctor.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_first_name_max_length(self):
        user = Doctor.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_last_name_label(self):
        user = Doctor.objects.get(id=1)
        field_label = user._meta.get_field('surname').verbose_name
        self.assertEqual(field_label, 'Фамилия')

    def test_last_name_max_length(self):
        user = Doctor.objects.get(id=1)
        max_length = user._meta.get_field('surname').max_length
        self.assertEqual(max_length, 255)
