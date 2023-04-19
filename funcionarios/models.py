from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from departamentos.models import Departamento
from empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT) #func so tem uma ligacao
    departamentos = models.ManyToManyField(Departamento) #criar list
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome