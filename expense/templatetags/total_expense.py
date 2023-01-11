from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum
from expense.models import Expense

register = template.Library()


@register.simple_tag
def get_total_expsense(default=0.00):
    ''' Calculate the total expense of all expense '''
    return intcomma(Expense.objects.aggregate(Sum('amount'))['amount__sum'] or default)
