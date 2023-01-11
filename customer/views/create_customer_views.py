
from django.shortcuts import redirect, render
from django.views import View

from customer.models import Customer


class CreateCustomer(View):
    ''' Create a new customer '''

    def get(self, request, *args, **kwargs):
        ''' Respond to GET request '''
        return render(request,  'customer/add_customer.html')

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        phone_number = request.POST.get('phone_number')
        customer_address = request.POST.get('customer_address')
        customer = Customer(
            user=request.user,
            name=customer_name,
            email=customer_email,
            phone_number=phone_number,
            address=customer_address,
        )
        customer.save()
        '''Provide a redirect on GET request.'''
        return redirect('customer_list')
