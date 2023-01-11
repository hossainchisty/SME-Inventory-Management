from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from expense.models import Expense, Type
from utility.helper.decorators.filter import _currentUser


@method_decorator(cache_page(60 * 3), name='dispatch')
class ManageExpense(LoginRequiredMixin, View):
    ''' List of all Expense '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20)
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'expense/manage_expense.html', context)


class ExpenseType(LoginRequiredMixin, View):
    ''' Expense type list '''

    @method_decorator(_currentUser())
    def get(self, request):
        type_list = Type.objects.all().order_by('-id')
        paginator = Paginator(type_list, 20)
        page_number = request.GET.get('page')
        expense_type = paginator.get_page(page_number)
        context = {
            'expense_type': expense_type
        }
        return render(request, 'expense/expense_type_list.html', context)
