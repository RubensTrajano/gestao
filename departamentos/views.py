
from django.views.generic import ListView
from .models import Departamento

# Create your views here.
class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa

        return Departamento.objects.filter(empresa=empresa_logada)
