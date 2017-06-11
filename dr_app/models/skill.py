from django.db import models
from . import User

class Skill(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50); 
    domain = models.CharField(max_length=50); 
    def __unicode__(self):
        return self.name
