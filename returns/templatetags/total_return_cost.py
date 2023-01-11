from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum

from returns.models import Return

register = template.Library()


@register.simple_tag
def get_total_return_cost(default=0.00):
    ''' Calculate the total return '''
    return intcomma(Return.objects.aggregate(Sum('grand_total'))['grand_total__sum'] or default)
