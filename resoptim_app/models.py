from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. \
                                          Up to 15 digits allowed.")
    phone = models.CharField(validators=[phoneRegex], blank=True, max_length=15) # validators should be a list
    website = models.URLField();
    summary = models.TextField();

class SocialProfile(models.Model):
    TWITTER = 'TW'
    GITHUB = 'GH'
    LINKEDIN = 'LI'

    SOCIAL_NETWORK_CHOICES = (
        (TWITTER, 'Twitter'),
        (GITHUB, 'Github'),
        (LINKEDIN, 'LinkedIn'),
    )

    user = models.ForeignKey(User, related_name="profiles")
    network = models.CharField(max_length=50);
    username = models.CharField(max_length=50);
    url = models.URLField(max_length=200);
    oauthToken = models.CharField(max_length=200);

class WorkEntry(models.Model):
    user = models.ForeignKey(User, related_name="work")
    company = models.CharField(max_length=200);
    position = models.CharField(max_length=200);
    website = models.URLField();
    summary = models.TextField();
    startDate = models.DateField();
    endDate = models.DateField();

class EducationEntry(models.Model):
    user = models.ForeignKey(User, related_name="education")

class SkillEntry(models.Model):
    user = models.ForeignKey(User, related_name="skills")
