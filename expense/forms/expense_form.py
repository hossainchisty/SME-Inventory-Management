from django.forms import ModelForm

from expense.models import Expense


class ExpenseForm(ModelForm):
    ''' Form asking for create expenses '''

    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user', ]
