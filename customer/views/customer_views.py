from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from customer.models import Customer


@method_decorator(cache_page(60 * 1), name='dispatch')
class CustomerList(LoginRequiredMixin, View):

    def get(self, request):
        '''
        This will reutrn list of customer
        '''
        customer_list = Customer.objects.all().order_by('-id')
        paginator = Paginator(customer_list, 10)
        page_number = request.GET.get('page')

        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'customers': page_object
        }
        return render(request, 'customer/customer_list.html', context)
