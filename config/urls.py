# flake8: noqa

from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Inventory Portal'
admin.site.site_title = 'SME Inventory Management'
admin.site.index_title = 'SME Inventory Management'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]
