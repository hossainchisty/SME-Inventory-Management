# flake8: noqa
from django.shortcuts import render

from customer.models import Customer
from expense.models import Expense, Type
from purchase.models import Purchase

__author__ = "Hossain Chisty"


def _currentUser():
    '''
    This decorator for authenticated users only, and filtering by the logged in user from the request, another user, even if logged in, can't access another user's data.
    '''
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            models = Expense
            models = Type
            models = Purchase
            models = Customer
            selected_user = models.objects.filter(user=request.user)
            if selected_user:
                return func(request, *args, **kwargs)
            else:
                return render(request, 'core/error/403.html')

        return wrapper
    return decorator
