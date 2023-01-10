from django.urls import path

from product.views.add_brand_views import CreateBrand
from product.views.add_category_views import CreateCategory
from product.views.add_product_views import CreateProduct
from product.views.product_views import BrandListView, CategoryListView, ProductListView
from product.views.update_brand_views import UpdateBrand
from product.views.update_category_views import UpdateCategory
from product.views.update_product_views import UpdateProductView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('catetory/list', CategoryListView.as_view(), name='category_list'),
    path('brand/list', BrandListView.as_view(), name='brand_list'),
    path('update/category/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('update/brand/<int:pk>', UpdateBrand.as_view(), name='update_brand'),
    path('add/catetory', CreateCategory.as_view(), name='add_category'),
    path('add/', CreateProduct.as_view(), name='add_product'),
    path('add/brand', CreateBrand.as_view(), name='add_brand'),
    path('update/<str:product_name>/<str:category>/<int:pk>', UpdateProductView.as_view(), name='update_product'), # noqa
]
