from django.db import models

class Especialidade(models.Model):
    description = models.CharField(max_length=200)
