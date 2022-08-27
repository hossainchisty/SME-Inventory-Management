from django.db import models

from utility.common_fields import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
