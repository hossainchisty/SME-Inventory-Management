from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum

from sale.models import Sale

register = template.Library()


@register.simple_tag
def get_total_sale(default=0.00):
    ''' Calculate the total sale of all sales. '''
    return intcomma(Sale.objects.aggregate(Sum('grand_total'))['grand_total__sum'] or default)
