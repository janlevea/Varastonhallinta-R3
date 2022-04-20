from django.contrib import admin
from django.urls import include, path

from varastonhallinta.views import index

urlpatterns = [
    path('', index),
    path('varasto/', include('varasto.urls')),
    path('admin/', admin.site.urls),
] 