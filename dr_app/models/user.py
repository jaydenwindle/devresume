from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from requests import get

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. \
                                          Up to 15 digits allowed.")
    phone = models.CharField(validators=[phoneRegex], blank=True, max_length=15) # validators should be a list
    website = models.URLField(blank=True);

    def save(self, *args, **kwargs):
        if self.pk is None:
            r = get('https://api.github.com/users/' + self.username).json()
            if r["name"]:
                self.name = r["name"] 
            if r["blog"]:
                self.website = r["blog"]
            if r["location"]:
                self.location = r["location"]
            if r["bio"]:
                self.bio = r["bio"]

        super(User, self).save(*args, **kwargs)
