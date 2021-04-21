from django.db import models

class Especialidade(models.Model):
    description = models.CharField(max_length=200)

class Profissional(models.Model):
    name = models.CharField(max_length=200)
    crm = models.CharField(max_length=50)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING)
