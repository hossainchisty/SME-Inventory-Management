from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from returns.models import Return


class ReturnView(LoginRequiredMixin, View):
    def get(self, request):
        ''' List of all Return'''
        return_list = Return.objects.all().order_by('-id')
        paginator = Paginator(return_list, 20)
        page_number = request.GET.get('page')
        return_list = paginator.get_page(page_number)
        context = {
            'return_list': return_list
        }
        return render(request, 'return/return_list.html', context)
