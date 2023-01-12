# Basic Lib Import
from django.urls import path

from brand.views.add_brand_views import CreateBrand
from brand.views.brand_list_views import BrandListView
from brand.views.update_brand_views import UpdateBrand

# Routing Implement
urlpatterns = [
    path('list', BrandListView.as_view(), name='brand_list'),
    path('update/<int:pk>', UpdateBrand.as_view(), name='update_brand'),
    path('add', CreateBrand.as_view(), name='add_brand'),
]
