from django.shortcuts import redirect, render
from django.views import View

from expense.forms.expense_form import ExpenseForm


class CreateExpense(View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request, *args, **kwargs):
        ''' Get the expense form '''
        return render(request,  'expense/add_expense.html', {'form': ExpenseForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new expense '''
        form = ExpenseForm(request.POST)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('expense_list')
        else:
            return render(request,  'expense/add_expense.html', {'form': ExpenseForm()})
