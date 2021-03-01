from django.db import models
from django.urls import reverse

class Ngo(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    whatsapp = models.IntegerField()
    city = models.CharField(max_length=254)
    ur = models.CharField(max_length=2)

    def get_absolute_url(self):
        return reverse('ngo_detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)


class Incidents(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    value = models.IntegerField()
    ngo = models.ForeignKey(Ngo, on_delete=models.SET_NULL, null=True)