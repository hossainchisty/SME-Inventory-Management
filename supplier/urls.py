from django.urls import path

from supplier.views.add_supplier_views import AddSupplier
from supplier.views.suppliers_list_views import SupplierList

urlpatterns = [
    path('list/', SupplierList.as_view(), name='suppliers_list'),
    path('add/', AddSupplier.as_view(), name='suppliers_add'),
]
