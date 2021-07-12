from users.models import CustomUser
from django.test import TestCase
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserTest(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='test',
            email='test@mail.com',
            password='testing321'
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        admin_user = CustomUser.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
