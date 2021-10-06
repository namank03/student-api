from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.


class UserTestCase(TestCase):
    def test_user(self):
        username = 'shetu'
        password = 'hello'
        u = User(username=username)
        u.set_password(password)
        u.save()
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))
