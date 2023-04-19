
from django.contrib import admin
from django.urls import path, include

import funcionarios

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('empresa/', include('empresas.urls')),
    path('departamentos/', include('departamentos.urls')),
]
