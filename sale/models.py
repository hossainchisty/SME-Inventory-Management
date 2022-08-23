from django.db import models

from customer.models import Customer
from utility.common_fields import BaseModel


class Sale(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vat_tax = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    other_cost = models.PositiveIntegerField(default=0)
    shipping_cost = models.PositiveIntegerField(default=0)
    grand_total = models.PositiveIntegerField(default=0)
    note = models.TextField()
