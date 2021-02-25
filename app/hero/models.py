from django.db import models


class Ong(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    whatsapp = models.IntegerField()
    city = models.CharField(max_length=254)
    ur = models.CharField(max_length=2)


class Incidents(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    value = models.IntegerField()
    ong = models.ForeignKey(Ong, on_delete=models.SET_NULL, null=True)
