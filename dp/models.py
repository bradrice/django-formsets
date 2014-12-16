from django.db import models
from django.forms.models import inlineformset_factory

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author)

