from django.test import TestCase
from user.models.user_model import User


class TestUserModel(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, '123')
