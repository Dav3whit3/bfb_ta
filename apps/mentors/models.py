from re import S
from statistics import mode
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


class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    mentors = models.ManyToManyField(Mentor, related_name='projects', through='Mentorship')

    def __str__(self) -> str:
        return self.name


class Mentorship(models.Model):
    id = models.AutoField(primary_key=True)

    id_mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        unique_together = [["id_mentor", "id_project"]]
