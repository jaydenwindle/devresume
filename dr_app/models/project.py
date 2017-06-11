from django.db import models
from . import User, Skill

class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects")
    name = models.CharField(max_length=200);
    gh_repo = models.URLField(max_length=200);
    website = models.URLField(max_length=200, blank=True);
    description = models.TextField();
    stars = models.IntegerField(blank=True, default=0);
    skills = models.ManyToManyField(Skill, blank=True)
