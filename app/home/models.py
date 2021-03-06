from django.db import models
from django.urls import reverse


class Bio(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='home/static/images', null=True)

    def __str__(self):
        return '{0}'.format(self.name) 


class Language(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image_name = models.CharField(max_length=50, null=True)
    image =  models.ImageField(upload_to='home/static/images', null=True)

    def get_absolute_url(self):
        return reverse('language_detail', args=[str(self.id)])

    
    def __str__(self):
        return '{0}'.format(self.name)

class Tool(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    short_description = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='home/static/images', null=True)

    def get_image(self):
        if self.img_photo and hasattr(self.img_photo, 'url'):
            return self.img_photo.url
        else:
            return '/path/to/default/image'

    def get_absolute_url(self):
        return reverse('tool_detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

class Job(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    tool = models.ManyToManyField(Tool, help_text="Tool used in the Job")
    image_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='home/static/images', null=True)


    def display_tool(self):
        return ', '.join(tool.name for genre in self.tool.all())

    display_tool.short_description = "Tool"

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
    

    def __str__(self):
        return '{0}'.format(self.name)
    
    
    
class Contact(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ["last_name"]
        
    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
        