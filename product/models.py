from django.db import models

from brand.models import Brand
from category.models import Category
from utility.common_fields import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    UNIT_CHOICES = (
        ('kilogram', 'Kilogram'),
        ('piece', 'Piece'),
        ('milligram', 'Milligram'),
        ('quintal', 'Quintal'),
        ('tonne', 'Tonne'),
        ('milliliter', 'Milliliter')
    )
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    in_stock = models.IntegerField(default=0)
    details = models.TextField()

    def __str__(self):
        return self.name
