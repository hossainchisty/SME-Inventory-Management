# Basic Lib Import
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from product.models import Brand


class UpdateBrand(UpdateView):
    model = Brand
    fields = ['name', ]
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brand_list')
