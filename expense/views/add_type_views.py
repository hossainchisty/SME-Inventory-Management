
from django.shortcuts import redirect, render
from django.views import View

from expense.models import Type


class CreateType(View):
    ''' Intentionally simple parent class for all views. '''
    def get(self, request, *args, **kwargs):
        return render(request,  'expense/add_type.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new expense '''
        type_name = request.POST.get('type')
        type = Type(name=type_name)
        type.save()
        """Provide a redirect on GET request."""
        return redirect('expense_type_list')
