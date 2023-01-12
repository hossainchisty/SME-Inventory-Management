# Basic Lib Import
from django.urls import path

from product.views.add_product_views import CreateProduct
from product.views.product_views import ProductListView
from product.views.update_product_views import UpdateProductView

# Routing Implement
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('add/', CreateProduct.as_view(), name='add_product'),
    path('update/<str:product_name>/<str:category>/<int:pk>', UpdateProductView.as_view(), name='update_product'), # noqa
]
