from .views import funcionarioList, funcionarioEdit, FuncionarioDelete, FuncionarioNovo
from django.urls import path

urlpatterns = [

    path('', funcionarioList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', funcionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),

]