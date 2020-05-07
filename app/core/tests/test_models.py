from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Testing create user success"""
        email = "olushola251@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalize(self):
        """test if the email of a new user is normalized"""
        email = 'reer@KKKKlllfd.com'
        password = '123456'

        user  = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_validate_email_field(self):
        """check if email field is provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "12345")
    
    def test_create_superuser(self):
        """check if email field is provided"""
        user = get_user_model().objects.create_superuser("olushola251@gmail.com", "password")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

