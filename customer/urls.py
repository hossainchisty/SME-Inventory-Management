
from django.urls import path

from customer.views.create_customer_views import CreateCustomer
from customer.views.customer_views import CustomerList
from customer.views.delete_customer_views import DeleteCustomer
from customer.views.update_customer_views import UpdateCustomer

urlpatterns = [
    path('list/', CustomerList.as_view(), name='customer_list'),
    path('add/', CreateCustomer.as_view(), name='add_customer'),
    path('update/<int:pk>/', UpdateCustomer.as_view(), name='update_customer'),
    path('delete/<pk>', DeleteCustomer.as_view(), name='delete_customer'),
]
