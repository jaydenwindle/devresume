from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
import requests
import math
from collections import Counter

class User(AbstractUser):
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
            r = requests.get('https://api.github.com/users/' + self.username + '/repos')
            print r.text
            super(User, self).save(*args, **kwargs)

class SkillEntry(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50); 
    domain = models.CharField(max_length=50); 
    def __unicode__(self):
        return self.name

class WorkEntry(models.Model):
    user = models.ForeignKey(User, related_name="work_history")
    company = models.CharField(max_length=200);
    position = models.CharField(max_length=200);
    website = models.URLField(blank=True);
    summary = models.TextField();
    skills = models.ManyToManyField(SkillEntry, blank=True)
    startDate = models.DateField();
    endDate = models.DateField();

class EducationEntry(models.Model):
    user = models.ForeignKey(User, related_name="education")
    institution = models.CharField(max_length=200); 
    area = models.CharField(max_length=200, verbose_name="Area of Study"); 
    skills = models.ManyToManyField(SkillEntry)
    startDate = models.DateField(verbose_name="Start Date"); 
    endDate = models.DateField(verbose_name="End Date"); 

class ProjectEntry(models.Model):
    user = models.ForeignKey(User, related_name="projects")
    name = models.CharField(max_length=200);
    gh_repo = models.URLField(max_length=200);
    website = models.URLField(max_length=200, blank=True);
    description = models.TextField();
    stars = models.IntegerField(blank=True, default=0);
    skills = models.ManyToManyField(SkillEntry, blank=True)

class ApplicationEntry(models.Model):
    user = models.ForeignKey(User, related_name="applications")
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    desired_skills = models.ManyToManyField(SkillEntry, blank=True)

class ApplicationProjectRelationship(models.Model):
    application = models.ForeignKey(ApplicationEntry, related_name="projects")
    project = models.ForeignKey(ProjectEntry, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6)

class ApplicationWorkRelationship(models.Model):
    application = models.ForeignKey(ApplicationEntry, related_name="jobs")
    work = models.ForeignKey(WorkEntry, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6)

class ApplicationEducationRelationship(models.Model):
    application = models.ForeignKey(ApplicationEntry, related_name="education")
    education = models.ForeignKey(EducationEntry, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6, blank=True)

@receiver(m2m_changed, sender=ApplicationEntry.desired_skills.through)
def add_application_data(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        user = instance.user
        for project in user.projects.all():
            sim = similarity(project.skills.all(), instance.desired_skills.all())
            p, new = instance.projects.get_or_create(project=project, defaults={"similarity": sim})
        for job in user.work_history.all():
            sim = similarity(job.skills.all(), instance.desired_skills.all())
            p, new = instance.jobs.get_or_create(work=job, defaults={"similarity": sim})
        for ed in user.education.all():
            sim = similarity(ed.skills.all(), instance.desired_skills.all())
            p, new = instance.education.get_or_create(education=ed, defaults={"similarity": sim})

def similarity(v1, v2):
    num_similar = 0
    for i in v1:
        if i in v2:
            num_similar += 1

    return num_similar
