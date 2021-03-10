from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from comment.models import Comment

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

class Post(models.Model):
    title= models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    text_body = models.TextField()
    comments = GenericRelation(Comment)

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('blog:post', args=[str(self.id)])

            
    class Meta:
        ordering = ['-created']
