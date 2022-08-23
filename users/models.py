from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from utility.common_fields import BaseModel

from .managers import CustomUserManager


class CustomUser(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'^(?:\+88|88)?(01[3-9]\d{8})$')
    phone_number = models.CharField(validators=[phone_regex], max_length=14, unique=True,
                                    help_text="Phone number must be entered in the format: '+8801XXXXXX'. Up to 14 digits allowed.")  # noqa
    avatar = models.ImageField(upload_to='media')

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.email
