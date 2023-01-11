from django import template
from django.db.models import Sum

from customer.models import Customer

register = template.Library()


@register.simple_tag
def total_customer():
    '''
    This method is used to get total customer.
    '''
    return Customer.objects.all().count()
