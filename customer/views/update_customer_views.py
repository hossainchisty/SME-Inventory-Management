from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from customer.models import Customer


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ['name', 'email', 'address', 'phone_number']
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
