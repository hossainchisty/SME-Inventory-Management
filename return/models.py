from django.db import models

from customer.models import Customer
from product.models import Product
from utility.common_fields import BaseModel


class ReturnSummary(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vat_tax = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    other_cost = models.PositiveIntegerField(default=0)
    shipping_cost = models.PositiveIntegerField(default=0)
    grand_total = models.PositiveIntegerField(default=0)
    note = models.TextField()


class Return(BaseModel):
    return_summary = models.ForeignKey(ReturnSummary,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    unit_cost = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
