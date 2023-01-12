# Basic Lib Import
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from category.models import Category


class CategoryListView(View):
    ''' This will reutrn list of category '''
    def get(self, request):
        category_list = Category.objects.all().order_by('-id')
        paginator = Paginator(category_list, 10)
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
            'category': page_object,
        }
        return render(request, 'category/category_list.html', context)
