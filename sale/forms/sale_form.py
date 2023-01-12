from django.forms import ModelForm
from django.forms.widgets import DateInput
from sale.models import Sale


class SaleForm(ModelForm):
    ''' Form asking for the Sales Information '''
    class Meta:
        model = Sale
        fields = ['customer', 'vat_tax', 'discount', 'other_cost', 'shipping_cost', 'grand_total', 'note']
        # widgets = {
        #     'date': DateInput(attrs={'type': 'date'})
        # }
