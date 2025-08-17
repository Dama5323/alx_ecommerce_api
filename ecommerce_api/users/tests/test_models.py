from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_email_uniqueness(self):
        User.objects.create_user(
            username='user1',
            email='test@example.com',
            password='testpass123'
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='user2',
                email='test@example.com',
                password='testpass123'
            )

    def test_username_uniqueness(self):
        User.objects.create_user(
            username='testuser',
            email='test1@example.com',
            password='testpass123'
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='testuser',
                email='test2@example.com',
                password='testpass123'
            )