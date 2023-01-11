from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from expense.models import Type


class UpdateType(UpdateView):
    ''' Update expense type '''
    model = Type
    fields = ['name', ]
    template_name = 'expense/expense_type_form.html'
    success_url = reverse_lazy('expense_type_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this expense.")
        return obj
