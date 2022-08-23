# flake8: noqa

from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'SME Inventory Management'
admin.site.site_title = 'SME Inventory Management'
admin.site.index_title = 'Inventory Portal'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
