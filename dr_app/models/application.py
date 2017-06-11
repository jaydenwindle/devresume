from django.db import models
from . import User, Skill, Project, Work, Education
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Application(models.Model):
    user = models.ForeignKey(User, related_name="applications")
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    desired_skills = models.ManyToManyField(Skill, blank=True)

class ApplicationProjectRelationship(models.Model):
    application = models.ForeignKey(Application, related_name="projects")
    project = models.ForeignKey(Project, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6)

class ApplicationWorkRelationship(models.Model):
    application = models.ForeignKey(Application, related_name="jobs")
    work = models.ForeignKey(Work, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6)

class ApplicationEducationRelationship(models.Model):
    application = models.ForeignKey(Application, related_name="education")
    education = models.ForeignKey(Education, related_name="applications")
    similarity = models.DecimalField(decimal_places=4, max_digits=6, blank=True)

@receiver(m2m_changed, sender=Application.desired_skills.through)
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
            print(ed)
            sim = similarity(ed.skills.all(), instance.desired_skills.all())
            p, new = instance.education.get_or_create(education=ed, defaults={"similarity": sim})

def similarity(v1, v2):
    num_similar = 0
    for i in v1:
        if i in v2:
            num_similar += 1

    return num_similar
