from django.db import models

# Create your models here.

class Canil(models.Model):

    class Meta:
        db_table = 'canil'

    nome = models.CharField(max_length=200)
    distancia = models.DecimalField(max_digits=5, decimal_places=2)
    caoPequenoFDS = models.DecimalField(max_digits=5, decimal_places=2)
    caoGrandeFDS = models.DecimalField(max_digits=5, decimal_places=2)
    caoPequeno = models.DecimalField(max_digits=5, decimal_places=2)
    caoGrande = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome