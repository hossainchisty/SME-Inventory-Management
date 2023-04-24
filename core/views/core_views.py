from django.shortcuts import render
from django.views.generic import View

class Dashboard(View):

    def get(self, request):
        return render(request, 'core/dashboard.html')