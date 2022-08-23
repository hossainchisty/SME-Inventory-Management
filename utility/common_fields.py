from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """ Abstract base classe some common information """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ['-created_at']
        abstract = True
