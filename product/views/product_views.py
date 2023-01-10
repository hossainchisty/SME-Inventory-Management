from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from product.models import Brand, Category, Product


class ProductListView(View):
    def get(self, request):
        ''' This will reutrn list of products '''
        product_list = Product.objects.all().order_by('-id')

        paginator = Paginator(product_list, 25)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        context = {
            'products': products,
        }
        return render(request, 'product/product_list.html', context)


class CategoryListView(View):
    def get(self, request):
        ''' This will reutrn list of category '''
        category_list = Category.objects.all().order_by('-id')
        paginator = Paginator(category_list, 25)
        page_number = request.GET.get('page')
        category = paginator.get_page(page_number)

        context = {
            'category': category,
        }
        return render(request, 'product/category_list.html', context)


class BrandListView(View):
    def get(self, request):
        ''' This will reutrn list of brand '''
        brand_list = Brand.objects.all().order_by('-id')
        paginator = Paginator(brand_list, 25)
        page_number = request.GET.get('page')
        brand = paginator.get_page(page_number)

        context = {
            'brand': brand,
        }
        return render(request, 'product/brand_list.html', context)
