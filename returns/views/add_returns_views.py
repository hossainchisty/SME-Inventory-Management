from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from returns.forms.returns_form import ReturnForm


class CreateReturn(View):
    ''' This class is used to create a new returns. '''

    def get(self, request, *args, **kwargs):
        ''' Get the returns form '''
        return render(request,  'return/add_return.html', {'forms': ReturnForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new returns '''

        form = ReturnForm(request.POST)
        with transaction.atomic():
            # Automatically set to the currently logged-in user
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                """Provide a redirect on GET request."""
                return redirect('return_list')
            else:
                return render(request, 'return/add_return.html', {'forms': form})
