
from django.shortcuts import redirect, render
from django.views import View

from product.models import Brand


class CreateBrand(View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request, *args, **kwargs):
        return render(request,  'product/add_brand.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new category '''
        brand_name = request.POST.get('brand_name')
        brand = Brand(name=brand_name)
        brand.save()
        """Provide a redirect on GET request."""
        return redirect('brand_list')
