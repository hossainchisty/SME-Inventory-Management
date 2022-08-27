from django.core.validators import RegexValidator
from django.db import models

from utility.common_fields import BaseModel


class Customer(BaseModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_regex = RegexValidator(
        regex=r'^(?:\+88|88)?(01[3-9]\d{8})$')
    phone_number = models.CharField(validators=[phone_regex], max_length=14, unique=True,
                                    help_text="Phone number must be entered in the format: '+8801XXXXXX'. Up to 14 digits allowed.")  # noqa

    def __str__(self):
        return self.name
