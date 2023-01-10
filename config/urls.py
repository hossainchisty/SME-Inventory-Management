# flake8: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += [
    path('', include('core.urls')),
    path('customer/', include('customer.urls')),
    path('supplier/', include('supplier.urls')),
    path('product/', include('product.urls')),

    path('users/', include('users.urls')),
]


schema_view = get_schema_view(
   openapi.Info(
      title="SME Inventory Management API",
      default_version='v1',
      description="Inventory management refers to the process of ordering, storing, using, and selling a company's inventory. This includes the management of raw materials, components, and finished products and processing of such items.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hossain.chisty11@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   path('swagger/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin panel configure
admin.site.site_header = 'SME Inventory Management'
admin.site.site_title = 'SME Inventory Management'
admin.site.index_title = 'Inventory Portal'
admin.autodiscover()