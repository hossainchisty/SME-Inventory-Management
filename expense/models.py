from django.db import models

from utility.common_fields import BaseModel


class Type(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Expense(BaseModel):
    name = models.CharField(max_length=150)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    note = models.TextField()

    def __str__(self):
        return self.name
