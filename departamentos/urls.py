from .views import DepartamentosList
from django.urls import path

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
]