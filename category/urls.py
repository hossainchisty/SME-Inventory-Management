# Basic Lib Import
from django.urls import path

from category.views.add_category_views import CreateCategory
from category.views.category_list_views import CategoryListView
from category.views.update_category_views import UpdateCategory

# Routing Implement
urlpatterns = [
    path('list', CategoryListView.as_view(), name='category_list'),
    path('update/category/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('add', CreateCategory.as_view(), name='add_category'),
]
