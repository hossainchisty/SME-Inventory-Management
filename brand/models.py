from django.db import models

from utility.common_fields import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
