import uuid
from datetime import date 

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


#class Genre(models.Model):
#    """ 
#    Model representing a book genre
#    """
#    name = models.CharField(
#        max_length=200, 
#        help_text='Enter a book genre (e.g. Science Fiction)'
#        )
#
#    def __str__(self):
#        """
#        String for representing the Model object.
#        """
#        return self.name
    

#class Language(models.Model):
#    """
#    Model representing a Language (e.g. English, French, Japanese, etc.)
#    """
#    name = models.CharField(max_length=200, 
#                            help_text="Enter the book's natural language (e.g. English, French, Japanese, etc)")
#
#    def __str__(self):
#        """String for representing the Model object (in Admin site etc.)"""
#        return self.name 


class Incident(models.Model):
    """
    Model representing a Incidents.
    """
    title = models.CharField(max_length=200)
    ngo = models.ForeignKey('Ngo', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the NGO')
    value = models.IntegerField()

    class Meta:
        ordering = ['title', 'ngo']

#    def display_genre(self):
#        """
#        Create a string for the Genre. This is required to display genre in Admin.
#        """
#        return ', '.join([ngo.name for ngo in self.ngo.all()[:3]])
#
#    display_ngo.short_description = 'Genre'    

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book
        """
        return reverse('hero:incident-detail', args=[str(self.id)])
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        

#class BookInstance(models.Model):
#    """
#    Model representing a specific copy of a book 
#    (i.e that can be borrowed from the library).
#    """
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                          help_text="Unique ID for this particular book across whole library")
#    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
#    imprint = models.CharField(max_length=200)
#    due_back = models.DateField(null=True, blank=True)
#    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#
#
#    @property
#    def is_overdue(self):
#        if self.due_back and date.today() > self.due_back:
#            return True
#        return False
#
#    LOAN_STATUS = (
#        ('d', 'Maintenance'),
#        ('o', 'On loan'),
#        ('a', 'Available'),
#        ('r', 'Reserved'),
#    )
#
#    status = models.CharField(
#        max_length=1,
#        choices=LOAN_STATUS,
#        blank=True,
#        default='d',
#        help_text='Book availability')
#
#    class Meta:
#        ordering = ['due_back']
#        permissions = (("can_mark_returned", "Set book as returned"),)
#
#    def __str__(self):
#        """
#        String for representing the Model object.
#        """
#        return '{0} ({1})'.format(self.id, self.book.title)

class Ngo(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    whatsapp = models.IntegerField()
    city = models.CharField(max_length=100)
    ur = models.CharField(max_length=2)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """
        Return the url to access a particular ngo instance.
        """
        return reverse('hero:ngo-detail', args=[str(self.id)])
            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}'.format(self.name)