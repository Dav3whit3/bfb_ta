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
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()


class Project(models.Model):
    _id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
   

class Mentorship(models.Model):
    mentorId = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)


""" ### Modern aproach
class Mentor(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Project(models.Model):
    name = models.CharField(max_length=30)
    mentors = models.ManyToManyField(Mentor) """