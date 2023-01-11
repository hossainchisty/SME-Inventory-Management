from django.db import models

from customer.models import Customer
from product.models import Product
from utility.common_fields import BaseModel


class Return(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    vat_tax = models.IntegerField(default=0)
    qty = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    other_cost = models.PositiveIntegerField(default=0)
    shipping_cost = models.PositiveIntegerField(default=0)
    grand_total = models.PositiveIntegerField(default=0)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.name
