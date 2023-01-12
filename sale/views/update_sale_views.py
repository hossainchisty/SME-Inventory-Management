from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from sale.models import Sale


class UpdateSale(UpdateView):
    ''' This view is used to update the sale model. '''
    model = Sale
    fields = ['customer', 'vat_tax', 'discount', 'other_cost', 'shipping_cost', 'grand_total', 'note', ]
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this sale.")
        return obj
