from django.test import TestCase
import re

from .models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(
            phone_number='+639485712486',
            first_name='John',
            last_name='Doe',
            email='',
            password='This is john doe'
        )

    def test_phone_number_regex(self):
        user = User.objects.get(id=1)
        phone_regex = re.compile('^(09|\+639)\d{9}$', re.I)
        match = phone_regex.match(str(user.phone_number))
        self.assertEqual(bool(match), True)

    def test_object_name_is_phone_number(self):
        user = User.objects.get(id=1)
        expected_object_name = user.phone_number
        self.assertEqual(str(user), expected_object_name)

    def test_object_get_username(self):
        user = User.objects.get(id=1)
        expected_username = user.phone_number
        self.assertEqual(user.get_username(), expected_username)

    def test_object_get_full_name(self):
        user = User.objects.get(id=1)
        expected_full_name = f'{user.first_name} {user.last_name}'
        self.assertEqual(user.get_full_name(), expected_full_name)

    