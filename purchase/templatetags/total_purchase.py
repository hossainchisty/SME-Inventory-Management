
from django import template
from django.db.models import Sum

from purchase.models import PurchaseSummary

register = template.Library()


@register.simple_tag
def get_total_purchase(defalut=0.00):
    '''
    This method is to calculate the total product cost
    '''
    return PurchaseSummary.objects.aggregate(Sum('grand_total'))['grand_total__sum'] or defalut
