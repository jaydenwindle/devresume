from django.db import models
from . import User, Skill

class Work(models.Model):
    user = models.ForeignKey(User, related_name="work_history")
    company = models.CharField(max_length=200);
    position = models.CharField(max_length=200);
    website = models.URLField(blank=True);
    summary = models.TextField();
    skills = models.ManyToManyField(Skill, blank=True)
    startDate = models.DateField();
    endDate = models.DateField();
