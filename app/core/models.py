from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Cannot create account without email")
        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        superuser = self.create_user(email, password)

        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """User model that accepts email and password"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
