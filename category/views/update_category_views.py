# Basic Lib Import
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from category.models import Category


class UpdateCategory(UpdateView):
    model = Category
    fields = ['name', ]
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')
