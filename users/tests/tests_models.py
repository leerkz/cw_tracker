from django.contrib.auth import get_user_model
from django.test import TestCase

class UserModelTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))

    def test_create_superuser(self):
        superuser = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        self.assertEqual(superuser.username, 'admin')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
