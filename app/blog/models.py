from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

class Post(models.Model):
    title= models.CharField(max_length=100)
    post_date = models.DateField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    text_body = models.TextField()

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

