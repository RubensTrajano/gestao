from django.db import models
from empresas.models import Empresa

class Departamento(models.Model):
    nome = models.CharField(max_length=70)

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome
