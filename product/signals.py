from django.db.models.signals import pre_save
from django.dispatch import receiver

from product.models import Product


@receiver(pre_save, sender=Product)
def track_product_stock(sender, instance, **kwargs):
    """ Tracks the product stock and updates the product stock status. """
    if instance.in_stock <= 0:
        print(f'{instance.name} is out of stock')
    else:
        print(f'{instance.name} is in stock')
