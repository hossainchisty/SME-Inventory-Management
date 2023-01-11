from django.urls import path

from returns.views.add_returns_views import CreateReturn
from returns.views.return_list_view import ReturnView

urlpatterns = [
    path('list/', ReturnView.as_view(), name='return_list'),
    path('add/', CreateReturn.as_view(), name='add_return'),
]
