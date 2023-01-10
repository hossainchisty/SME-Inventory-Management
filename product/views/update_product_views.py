from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from product.models import Product


class UpdateProductView(UpdateView):
    """ Update product view """
    model = Product
    fields = ['name', 'category', 'brand', 'unit', 'details'] # noqa
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('product_list')
