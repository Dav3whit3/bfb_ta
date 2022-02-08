from re import S
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STATUS_CHOICES = (
    ('active', 'active'),
    ('deleted', 'deleted'),
)


# Create your models here.

class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=30)


class Mentor(models.Model):
    id_mentor = models.AutoField(primary_key=True)
    mentor_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    projects = models.ManyToManyField(Project,
                                      related_name='name',
                                      through="Mentorship")
    def __str__(self) -> str:
        return self.mentor_name


class Mentorship(models.Model):
    id_project_mentor = models.AutoField(primary_key=True)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ["mentorId", "projectId"]
