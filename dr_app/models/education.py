from django.db import models
from . import Skill, User

class Education(models.Model):
    user = models.ForeignKey(User, related_name="education")
    institution = models.CharField(max_length=200); 
    area = models.CharField(max_length=200, verbose_name="Area of Study"); 
    skills = models.ManyToManyField(Skill)
    startDate = models.DateField(verbose_name="Start Date"); 
    endDate = models.DateField(verbose_name="End Date"); 
