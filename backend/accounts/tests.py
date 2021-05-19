from django.test import TestCase
import re

from .models import Profile, User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create(
            phone_number='+639485712486',
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='',
            password='This is john doe'
        )
        
        Profile.objects.create(user=user)

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

    def test_object_get_short_name(self):
        user = User.objects.get(id=1)
        expected_short_name = user.first_name
        self.assertEqual(user.get_short_name(), expected_short_name)
    
    # Profile tests 
    
    def test_profile_user_id(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user_id=1)
        self.assertEqual(profile.user_id, user.id)

    def test_profile_slug_is_user_username(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(user_id=1)
        self.assertEqual(user.username, profile.slug)