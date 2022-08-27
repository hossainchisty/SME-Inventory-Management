from django.db import models

from product.models import Product
from supplier.models import Supplier
from utility.common_fields import BaseModel


class PurchaseSummary(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    vat_tax = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    other_cost = models.PositiveIntegerField(default=0)
    shipping_cost = models.PositiveIntegerField(default=0)
    grand_total = models.PositiveIntegerField(default=0)
    note = models.TextField()


class Purchase(BaseModel):
    purchase_summary = models.ForeignKey(PurchaseSummary,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    unit_cost = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
