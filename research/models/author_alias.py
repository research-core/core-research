from django.db import models

class AuthorAlias(models.Model):

    name   = models.CharField('Alias', max_length=250)  #: Name
    person = models.ForeignKey('humanresources.Person', on_delete=models.CASCADE)