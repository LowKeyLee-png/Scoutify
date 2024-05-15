from django.db import models
from django_countries.fields import CountryField
from django_countries import countries

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    country = CountryField(choices=countries)
    def __str__(self):
        return self.username
