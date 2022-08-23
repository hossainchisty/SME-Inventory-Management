from django.db import models

from utility.common_fields import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150)
